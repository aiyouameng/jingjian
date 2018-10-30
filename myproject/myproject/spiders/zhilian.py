# -*- coding: utf-8 -*-
import scrapy
import json, re
from myproject.items import MyprojectItem, GwItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'

    # start_urls = ['http://quotes.toscrape.com/page/1/',
    #               'http://quotes.toscrape.com/page/2/', ]

    def start_requests(self):
        urls = [
            'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22jl%22:%22530%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D&_v=0.22712104&x-zp-page-request-id=9be8ca5eccf34b7da20009fd3b29a9c0-1540864422359-483615',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsondata = json.loads(response.text)
        result = jsondata["data"]["results"]
        for item in result:
            myitem = MyprojectItem()
            deurl = item["positionURL"]
            myitem["jobname"] = item["jobName"]
            myitem["salary"] = item["salary"]
            myitem["companyName"] = item["company"]["name"]
            # yield myitem
            yield scrapy.Request(deurl, callback=self.parse22, meta={"istem": myitem})

    def parse22(self, response):
        myitem = response.meta["istem"]
        body = response.text.replace("\n", '')
        info = re.findall('class="pos-ul">(.*?)</div>', body)
        # myitem = GwItem()
        if len(info) > 0:
            myitem["gwms"] = info[0]
        yield myitem
