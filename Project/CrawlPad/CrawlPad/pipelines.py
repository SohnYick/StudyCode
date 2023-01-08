# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl

class CrawlpadPipeline:

    def open_spider(self,spider):
        # 打开工作薄
        wb = openpyxl.Workbook()
        # 使用默认选择的工作表
        ws = wb.active
        ws.title = "bscpad"
        # 插入表头
        ws.append(("Project Name","Short Desc","index","twitter","medium","telegram"))

        # 绑定到对象，便于之后使用
        self.wb = wb
        self.ws = ws

    def close_spider(self,spider):
        # 保存工作簿
        self.wb.save("所有pad.xlsx")


    def process_item(self, item, spider):
        self.ws.append((
            item.get("title"),
            item.get("short_desc"),
            item.get("socials")["index"],
            item.get("socials")["twitter"],
            item.get("socials")["medium"],
            item.get("socials")["telegram"],
        ))
        return item
