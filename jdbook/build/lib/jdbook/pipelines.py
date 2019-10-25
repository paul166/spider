# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import json
from scrapy.exporters import JsonItemExporter

client = MongoClient('localhost',port=27017)
collection = client["jd"]["book1"]


class JdbookMongoPipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item))
        return item


class JdbookJsonPipeline(object):
    def open_spider(self,spider):
        self.filename = open('book.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        # with open('temp.txt','a',encoding='utf-8')as f :
        #     f.write(json.dumps(dict(item),ensure_ascii=False,indent=2))

        self.filename.write(json.dumps(dict(item),ensure_ascii=False) +'\n')
        return item

    def close_spider(self,spider):
        self.filename.close()


class JdbookJsonPipelines(object):
    def open_spider(self,spider):
        self.file = open('book.json','wb')

        self.writer = JsonItemExporter(self.file)
        self.writer.start_exporting()

    def process_item(self,item,spider):
        self.writer.export_item(item)
        return item

    def close_spider(self,spider):
        self.writer.finish_exporting()
        self.file.close()
