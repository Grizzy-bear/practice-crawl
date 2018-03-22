# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    novel_name = scrapy.Field()
    # novel_name_urls
    novel_name_author = scrapy.Field()
    novel_name_urls = scrapy.Field()
    novel_name_num = scrapy.Field()
    novel_chapter = scrapy.Field()
    novel_chapter_urls = scrapy.Field()
