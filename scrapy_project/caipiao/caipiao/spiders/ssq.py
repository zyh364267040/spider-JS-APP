import scrapy
from caipiao import items


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['sina.com.cn']
    # 起始url
    start_urls = ['https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs']

    def parse(self, response):
        # 使用xpath()获取所有tr
        tr_list = response.xpath('//*[@id="cpdata"]/tr')
        # 从tr中获取每期球号
        for tr in tr_list:
            date = tr.xpath('./td/text()').extract_first()
            if not date:
                continue
            red_ball = tr.xpath('./td[@class="chartball01" or @class="chartball20"]/text()').extract()
            blue_ball = tr.xpath('./td[@class="chartball02"]/text()').extract_first()

            # 把数据放到item中
            caipiao = items.CaipiaoItem()
            caipiao['date'] = date
            caipiao['red_ball'] = red_ball
            caipiao['blue_ball'] = blue_ball

            # 返回数据
            yield caipiao
