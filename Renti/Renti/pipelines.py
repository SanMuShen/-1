# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# 导入这个包为了移动文件
import shutil
# 导入项目设置
from scrapy.utils.project import get_project_settings

import os

class RentiPipeline(ImagesPipeline):

    # # 从项目设置文件中导入图片下载路径
    img_store = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        # print("*******************************")
        # print(item['img_path'])
        # print(item['img_name'])
        # print(item['img_url'])
        # print("*******************************")
        img_url = item['img_url']

        yield scrapy.Request(img_url)

    # 重写item_completed方法
    # 将下载的文件保存到不同的目录中
    # 参数 results 为下载图片的结果数组，包含下载后的路径以及是否成功下载
    def item_completed(self, results, item, info):
        
        # 从项目设置文件中导入图片下载路径
        image_path = [x["path"] for ok, x in results if ok]

        # 定义分类保存的路径
        img_path = "%s%s"%(self.img_store, item['img_path'].split('-')[0])
        # 目录不存在则创建目录
        if os.path.exists(img_path) == False:
            os.mkdir(img_path)

        # 将文件从默认下路路径移动到指定路径下
        shutil.move(self.img_store + image_path[0], img_path + "\\" + item["img_name"] + '.jpg')

        item["img_path"] = img_path + "\\" + item["img_name"] + '.jpg'

        return item
