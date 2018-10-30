# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    gwms=scrapy.Field()
    pass


class GwItem(scrapy.Item):
    gwzz = scrapy.Field()

class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    gwms=scrapy.Field()
    pass