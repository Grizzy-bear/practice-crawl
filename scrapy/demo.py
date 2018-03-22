# -*- coding: utf-8 -*-
import scrapy
from zimuku.items import ZimkuItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.net']
    start_urls = ['http://zimuku.net/']

    def parse(self, response):
        name = response.xpath('//b/text()').extract()[1]
        items = {}
        items['the first'] = name
        return items
