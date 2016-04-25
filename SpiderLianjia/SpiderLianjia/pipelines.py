# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
import sys

class SpiderlianjiaPipeline(object):
    def process_item(self, item, spider):
        return item

class xinfangLianjiaPipeline(object):
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
    def process_item(self,item,spider):
        #判断是否为链家新房爬虫
        if spider.name != 'xinfangLianjia':
            return item

        #判断是否存在历史价格数据
        if not item['houseHistoryPrice']:
            return item

        #打开写入的文件和CSV写入模块
	self.file = open('xinfangLianjia.csv','ab')
        csvWriter = csv.writer(self.file)

        #列表化时间、房价数据
        time_list = item['houseHistoryPrice']['time'].strip('[]').replace('"','').split(',')
        price_chengjiao_list = item['houseHistoryPrice']['price_chengjiao'].strip('[]').split(',')
        price_guapai_list = item['houseHistoryPrice']['price_guapai'].strip('[]').split(',')
        
        #格式化item为CSV格式数据
        for house in time_list:
            price_index = time_list.index(house)
            price_chengjiao = price_chengjiao_list[price_index]
            price_guapai = price_guapai_list[price_index]
            line = (house,item['houseName'],item['houseCity'],price_chengjiao,price_guapai,item['houseAddress'],item['houseBaiduLatitude'],item['houseBaiduLongitude'],item['houseTitle'])
            csvWriter.writerow(line)

        return item

class ershoufangLianjiaPipeline(object):
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
    def process_item(self,item,spider):
        if spider.name != 'ershoufangLianjia':
            return item

        #判断是否存在历史价格数据
        if not item['houseHistoryPrice']:
            return item

        #打开写入的文件和CSV写入模块
	self.file = open('ershoufangLianjia.csv','ab')
        csvWriter = csv.writer(self.file)

        #格式化item为CSV格式数据
        for house in item['houseHistoryPrice']['time']:
            price_index = item['houseHistoryPrice']['time'].index(house)
            price_chengjiao = item['houseHistoryPrice']['price'][price_index]
            price_guapai = item['houseHistoryPrice']['price'][price_index]
            line = (house,item['houseName'],item['houseCity'],price_chengjiao,price_guapai,item['houseArea'],'N/A',item['houseBaiduLatitude'],item['houseBaiduLongitude'],item['houseTitle'])
            csvWriter.writerow(line)


        return item

class zufangLianjiaPipeline(object):
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
    def process_item(self,item,spider):
        if spider.name != 'zufangLianjia':
            return item

        #判断是否存在历史价格数据
        if not item['houseHistoryPrice']:
            return item

        #打开写入的文件和CSV写入模块
	self.file = open('zufangLianjia.csv','ab')
        csvWriter = csv.writer(self.file)

        #格式化item为CSV格式数据
        for house in item['houseHistoryPrice']['time']:
            price_index = item['houseHistoryPrice']['time'].index(house)
            price_chengjiao = item['houseHistoryPrice']['price'][price_index]
            price_guapai = item['houseHistoryPrice']['price'][price_index]
            line = (house,item['houseName'],item['houseCity'],price_chengjiao,price_guapai,item['houseArea'],'N/A',item['houseBaiduLatitude'],item['houseBaiduLongitude'],item['houseTitle'])
            csvWriter.writerow(line)

        return item