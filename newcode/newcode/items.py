# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewcodeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()  # 名称
    meeting = scrapy.Field()  # 内推
    resume = scrapy.Field()  # 网申
    written = scrapy.Field()  # 笔试
    audition = scrapy.Field() # 面试
    send_offer = scrapy.Field()  # offer

