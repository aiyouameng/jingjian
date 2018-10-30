# -*- coding: utf-8 -*-
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from myproject.items import MyprojectItem, GwItem, LagouItem


class MyprojectPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client.zhilian1030

    def process_item(self, item, spider):
        table = ""
        if isinstance(item, MyprojectItem):
            table = self.db.zhilian
        elif isinstance(item, GwItem):
            table = self.db.gwtable
        elif isinstance(item, LagouItem):
            table = self.db.lagou
        table.insert_one(dict(item))
        print(item)
        return item

# class Myproject333Pipeline(object):
#     def __init__(self):
#         client = pymongo.MongoClient()
#         self.db = client.zhilian1030
#
#     def process_item(self, item, spider):
#         table = ""
#         if isinstance(item, MyprojectItem):
#             table = self.db.zhilian
#         elif isinstance(item, GwItem):
#             table = self.db.gwtable
#         table.insert_one(dict(item))
#         print(item)
#         return item
