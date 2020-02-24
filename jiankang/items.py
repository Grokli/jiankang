# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiankangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    occur_time = scrapy.Field()
    ask = scrapy.Field()
    ask_time = scrapy.Field()
    flags = scrapy.Field()
    doctor = scrapy.Field()
    position = scrapy.Field()
    hospital = scrapy.Field()
    category = scrapy.Field()
    answer = scrapy.Field()
    answer_time = scrapy.Field()
