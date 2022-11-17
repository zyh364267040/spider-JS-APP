# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo


class CaipiaoPipeline:
    # scrapy打开文件固定格式
    def open_spider(self, spider_name):
        self.f = open('ssq.csv', 'w', encoding='utf-8')

    # scrapy关闭文件固定格式
    def close_spider(self, spider_name):
        self.f.close()

    def process_item(self, item, spider):
        # 把得到的数据存到文件内
        self.f.write(item['date'])
        self.f.write(',')
        self.f.write('_'.join(item['red_ball']))
        self.f.write(',')
        self.f.write(item['blue_ball'])
        self.f.write('\n')

        return item


# 存入mysql
class CaipiaoMysqlPipeline:
    def open_spider(self, spider_name):
        # 连接mysql
        self.conn = pymysql.connect(
            host='192.168.228.2',
            port=3306,
            database='caipiao',
            user='root',
            password='mysql',
        )

    def close_spider(self, spider_name):
        self.conn.close()

    def process_item(self, item, spider):
        # 存储数据
        try:
            cur = self.conn.cursor()
            date = item['date']
            red_ball = item['red_ball']
            blue_ball = item['blue_ball']

            sql = f'insert into ssq(date, red_ball, blue_ball) values ("{date}", "{red_ball}", "{blue_ball}")'
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            if cur:
                cur.close()
            self.conn.rollback()

        return item


class CaipiaoMongoPipeline:
    def open_spider(self, spider_name):
        self.conn = pymongo.MongoClient(
            host='192.168.228.2',
            port=27017,
        )
        self.db = self.conn['caipiao']

    # scrapy关闭文件固定格式
    def close_spider(self, spider_name):
        self.conn.close()

    def process_item(self, item, spider):
        # 把得到的数据存到文件内
        self.db.ssq.insert_one({
            'date': item['date'],
            'red_ball': item['red_ball'],
            'blue_ball': item['blue_ball']
        })

        return item
