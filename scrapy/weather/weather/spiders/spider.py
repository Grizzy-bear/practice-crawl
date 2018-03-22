import scrapy
from weather.items import WeatherItem
class SztianqiSpider(scrapy.Spider):
    name = 'SZtianqi'
    allowed_domains = ["tianqi.com"]

    # 建立需要爬取信息的url列表
    start_urls = []
    # 需要爬的城市名称
    citys = ['nanjing', 'suzhou','shanghai']

    for city in citys:
        start_urls.append('http://' + city + '.tianqi.com')

    def parse(self, response):
        '''  
        data = 今日日期
        week = 星期
        img = 图标
        temp = 温度
        weather = 天气
        wind = 风向
        '''
        # 保存每天的信息
        item = []
        
        sixday = response.xpath('/html/body/div[2]/div/div[2]/div[2]')

        for day in sixday:
            item = WeatherItem()
            data = ''
            for datatitle in day.xpath('./ul[1]/li/b//text()').extract()[0]:
                data += datatitle
            item['date'] = data
            item['week'] = day.xpath('./p//text()').extract()[0]
            item['img'] = day.xpath(
                './ul/li[@class="tqpng"]/img/@src').extract()[0]
            tq = day.xpath('./ul/li[2]//text()').extract()
            # 我们用第二种取巧的方式，将tq里找到的str连接
            item['temperature'] = ''.join(tq)
            item['weather'] = day.xpath('./ul/li[3]/text()').extract()[0]
            item['wind'] = day.xpath('./ul/li[4]/text()').extract()[0]
            items.append(item)
        return items