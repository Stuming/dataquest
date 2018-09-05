# -*- coding: utf-8 -*-
import scrapy
from newcode.items import NewcodeItem


class JobScheduleSpider(scrapy.Spider):
    name = 'job_schedule'
    # allowed_domains = ['https://www.nowcoder.com/activity/campus2019']
    start_urls = ['https://www.nowcoder.com/activity/campus2019/']

    def parse(self, response):
        job_info = NewcodeItem()
        job_info['company'] = '公司'
        job_info['meeting'] = '内推时间'
        job_info['resume'] = '网申时间'
        job_info['written'] = '笔试时间'
        job_info['audition'] = '面试时间'
        job_info['send_offer'] = 'offer'
        yield job_info 

        job_list = response.xpath('//ul[@id="jsItemsList"]//div[@class="act-company-body"]')
        for job in job_list:
            job_info['company'] = job.xpath('.//h2/text()').extract()
            job_info['meeting'] = job.xpath('.//div[@class="act-company-info meeting"]/span[@class="act-company-time"]/text()').extract()
            job_info['resume'] = job.xpath('.//div[@class="act-company-info resume"]/span[@class="act-company-time"]/text()').extract()
            job_info['written'] = job.xpath('.//div[@class="act-company-info written"]/span[@class="act-company-time"]/text()').extract()
            job_info['audition'] = job.xpath('.//div[@class="act-company-info audition"]/span[@class="act-company-time"]/text()').extract()
            job_info['send_offer'] = job.xpath('.//div[@class="act-company-info send-offer"]/span[@class="act-company-time"]/text()').extract()

            yield job_info


