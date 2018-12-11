# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片存储路径  模特莫晨08年11月8日室拍-第46张 全部54P - 666人体艺术
    img_path = scrapy.Field()
    # 图片名字
    img_name = scrapy.Field()
    # 图片URL
    img_url = scrapy.Field()
