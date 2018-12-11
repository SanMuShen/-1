# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Renti.items import RentiItem

class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['www.666rt.me']
    start_urls = ['http://www.666rt.me/ArtZG/']

    rules = (
        Rule(LinkExtractor(allow=r'/list\d+.html')),
        Rule(LinkExtractor(allow=r'\d+/$')),
        Rule(LinkExtractor(allow=r'\d+/\d+.html'), callback='parse_item', follow=True),
    )
    
    # http://p.666rt.me/pic/2018/0601/670-lp.jpg
    def parse_item(self, response):
        item = RentiItem()
        # //div[@class="fzltp"]/ul/li/a/img/@src
        item['img_name'] = response.xpath('//div[@class="imgbox"]/a/img/@alt').extract()[0]
        item['img_path'] = response.xpath('//title/text()').extract()[0]
        item['img_url'] = response.xpath('//div[@class="imgbox"]/a/img/@src').extract()[0]
        
        return item
