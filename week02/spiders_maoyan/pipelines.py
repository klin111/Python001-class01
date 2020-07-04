# -*- coding: utf-8 -*-
import pandas as pd 
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
dic_info ={'name':[],'type':[],'atime':[]}
path='./scrapy-xpath.csv'


class SpidersMaoyanPipeline:
    def process_item(self, item, spider):
        # dic_info['name']=[item['Name']]
        # dic_info['type']=[item['Type']]
        # dic_info['atime']=[item['Time']]
        # pd.DataFrame(dic_info).to_csv(path, mode='a',index=False,encoding='utf8')
        conn = pymysql.connect(host = '192.168.0.107',
                                port = 3306,
                                user = 'root',
                                password = 'root',
                                database = 'test',
                                charset = 'utf8'
                                )

        cur=conn.cursor()

        result=[]
        # values=(item['Id'],item['Name'],item['Type'],item['Time'])
        values=(item['Name'],item['Type'],item['Time'])

        try:
            # cur.execute('insert into '+'film.film_name '+' values(%s,%s,%s,%s)',values)
            cur.execute('insert into '+'film.film_name(name,type,atime) '+' values(%s,%s,%s)',values)
            # cur.execute('select * from film.film_name')
            result.append(cur.fetchall())
            cur.close()
            conn.commit()

            print(result)

        except Exception as a:
            print(a)

        conn.close()
        return item

