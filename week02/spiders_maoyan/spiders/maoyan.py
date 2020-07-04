# -*- coding: utf-8 -*-
import scrapy
from spiders_maoyan.items import SpidersMaoyanItem
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

            item = SpidersMaoyanItem()
            item['Name'] = m.xpath('./div[1]/span[1]/text()').extract_first()
            item['Type'] = m.xpath('./div[2]/text()').extract()[1].split('\n')[1].strip()
            item['Time'] = m.xpath('./div[4]/text()')[1].extract().split('\n')[1].strip()
            item['Id']=n

            # print('-------------------')
            # print(item['Id'])
            # print(item['Name'])
            # print('-------------------')

            n += 1
            yield item
