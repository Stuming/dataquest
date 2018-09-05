# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class SxsInternSpider(scrapy.Spider):
    name = 'sxs_intern'
    allowed_domains = ['shixiseng.com']
    start_urls = ['https://www.shixiseng.com/']

    def parse(self, response):
        city_box = response.xpath('//div[@class="city-box"]//ul[@class="more-city"]//li[@class="md_hid"]')
        self.city_list = {}
        for city_info in city_box:
            city_name = city_info.xpath('./text()').extract()
            city_code = city_info.xpath('./@data-val').extract()
            self.city_list[city_name] = city_code

        if intern_url:
            scrapy.Request(intern_url, call_back=self.search_parse)
        else:
            raise ValueError('intern_url is unavailable')

    def search_parse(self, response):
        intern_box = response.xpath('//div[@class="position-list-box"]/


    def make_start_urls(self, job='数据', city='北京', pages=100, release_time='ft-wek'):


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(SxsInternSpider)
    process.start()

