# -*- coding: utf-8 -*-
import scrapy


class LinkedinSpider(scrapy.Spider):
    name = 'LinkedIn'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        pass
