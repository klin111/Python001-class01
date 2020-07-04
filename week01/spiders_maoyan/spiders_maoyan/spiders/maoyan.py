# -*- coding: utf-8 -*-
#倒入自带框架
import scrapy
#倒入要保存的列表项
from spiders_maoyan.items import SpidersMaoyanItem
#倒入框架自带的选择器，也就是lxml 包封装的过滤器
from scrapy.selector import Selector 


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']


    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        movies_info=Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        n = 0
        for m in movies_info:
            if n >= 10:
                break

            items = SpidersMaoyanItem()
            items['Name'] = m.xpath('./div[1]/span[1]/text()').extract_first()
            items['Type'] = m.xpath('./div[2]/text()').extract()[1].split('\n')[1].strip()
            items['Time'] = m.xpath('./div[4]/text()')[1].extract().split('\n')[1].strip()

            n += 1
            yield items
