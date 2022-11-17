# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class TuPipeline:
    def process_item(self, item, spider):
        # print(item['img_src'])
        return item


class DownloadTuPipeline(ImagesPipeline):
    # 1. 发送请求(下载图片, 文件, 视频, ...)
    def get_media_requests(self, item, info):
        url = item['img_src']
        yield scrapy.Request(url=url)

    # 2. 图片的存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        img_path = 'dongman'
        file_name = item['img_src'].split('/')[-1]
        real_path = img_path + '/' + file_name
        print(real_path)
        return real_path

    # 3. 可能需要对item进行更新
    def item_completed(self, results, item, info):
        return item
