# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixisengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()  # 工作名称
    refresh_time = scrapy.Field()  # 刷新时间
    job_money = scrapy.Field()  # 工资
    position = scrapy.Field()  # 城市
    academic = scrapy.Field()  # 学历
    week = scrapy.Field()  # 每周实习天数
    month = scrapy.Field()  # 实习月份
    good = scrapy.Field()  # 职位诱惑
    detail = scrapy.Field()  # 具体要求
    com_name = scrapy.Field()  # 公司名称
    com_position = scrapy.Field()  # 公司地点
    deadline = scrapy.Field()  # 应聘截止日期
    url = scrapy.Field()  # 网址

