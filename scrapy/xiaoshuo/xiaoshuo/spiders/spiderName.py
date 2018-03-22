import scrapy
from xiaoshuo.items import XiaoshuoItem

class xiaoshuospider(scrapy.Spider):

    name = 'xiaoshuoname'
    allowed_domains = ["qu.la"]

    def parse(self, response):
        '''  
        book names
        '''
        item = []
        items = []

        book_names_As = response.xpath("//*[@id="hotcontent"]/div[1]")

        for book_name_A in book_names_As :
            item = XiaoshuoItem()

            item['novel_name'] = book_name_A.xpath('./div[1]/dl/dt/a/text()').extract()[0]
            item['author'] = book_name_A.xpath('./div[1]/dl/dt/span/text()').extract()[0]
            item['novel_name_urls'] = book_name_A.xpath('//*[@id="hotcontent"]/div[1]/div[1]/dl/dt/a/@href')
            
            items.append(item)
        return items
            
