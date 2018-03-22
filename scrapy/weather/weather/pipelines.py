# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json
import codecs
import pymongo

class weatherPipeline(object):
    def process_item(self, item, spider):
        '''  
        处理每一个来自Spider传输过的
        '''
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.txt'
        # 在内存写入数据
        with open(filename, 'a') as f:
            f.write(item['data']+'\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature']+'\n')
            f.write(item['weather'] +'\n')
            f.write(['wind'] + '\n\n')
        
        # 下载数据
        with open(base_dir + '/data/' + item['data'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)
        return item

class w3json(object):
    def process_item(self, item, spider):
        '''  
        爬取的信息保存到json
        '''
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        # 打开json文件，向里面dump方式吸入数据
        # ensure_ascli=False,不然数据直接为utf编码方式
        with codecs.open(filename,'a') as f:
            line = json.dump(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

class w2mymonogo(object):
    def process_item(self, item, spider):
        '''  
        爬取的信息保存到数据库
        '''
        pass