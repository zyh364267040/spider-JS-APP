import scrapy


class Game4399Spider(scrapy.Spider):
    name = 'game_4399'
    allowed_domains = ['4399.com']
    start_urls = ['https://www.4399.com/flash/game100.htm']

    def parse(self, response):
        li_list = response.xpath('//*[@id="list"]/li')
        for li in li_list:
            name = li.xpath('./div/a//text()').extract_first()
            leibie = li.xpath('./span/a/text()').extract_first()
            shijian = li.xpath('./span[2]/text()').extract_first()
            # print(name, leibie, shijian)

            yield {'name': name, 'leibie': leibie, 'shijian': shijian}
