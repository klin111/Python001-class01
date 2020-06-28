# -*- coding: utf-8 -*-
import pandas as pd 

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
dic_info ={'name':[],'type':[],'atime':[]}
path='scrapy-xpath.csv'
class SpidersMaoyanPipeline:
    def process_item(self, item, spider):
        dic_info['name']=[item['Name']]
        dic_info['type']=[item['Type']]
        dic_info['atime']=[item['Time']]
        
        pd.DataFrame(dic_info).to_csv(path, mode='a',index=False,encoding='utf8')
        return item
