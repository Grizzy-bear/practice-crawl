'''
#@Author: Grizlly 
# @Date: 2018-03-13 19:12:33 
# -*- coding: utf-8 -*- 
'''
import scrapy 
from tutorial.items import TutorialItem

class Hotspder(scrapy.Spider):
    name = "hotspder"
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in range(1,3):
        start_urls.append('http://www.qiushibaike.com/8hr/page/'+str(i)+'/')
    
    def parse(self, response):
        item = TutorialItem()
        main = response.xpath('//div[@id="content-left"]/div')

        for div in main:
            #段子作者
            item['author'] = div.xpath('.//h2/text()').extract()[0]
            #段子主体
            item['body'] = ''.join(div.xpath('a[@class="contentHerf"]/div/span[1]/text()').extract())
            #footer
            item['funNum'] = div.xpath('.//span[@class="stats-vote"]/i/text()').extract()[0]
            item['comNum']= div.xpath('.//span[@class="stats-comments"]/a/i/text()').extract()[0]
            yield item
        
