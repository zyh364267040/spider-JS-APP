import scrapy
from tu import items


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/dongman/']

    def parse(self, response):
        li_list = response.xpath('//*[@class="pic-list2  clearfix"]/li')
        for li in li_list:
            href = li.xpath('./a/@href').extract_first()
            if href.endswith('.exe'):
                continue

            href = response.urljoin(href)

            yield scrapy.Request(
                url=href,
                method='get',
                callback=self.parse_dongman
            )

    def parse_dongman(self, response):
        img_src = response.xpath('//*[@id="bigImg"]/@src').extract_first()
        print('parse_dongman:', img_src)
        tu_item = items.TuItem()
        tu_item['img_src'] = img_src

        yield tu_item
