import scrapy

class CrawlpadItem(scrapy.Item):
    # define the fields for your item here like:
    # 项目名
    title = scrapy.Field()
    # 项目简述
    short_desc = scrapy.Field()
    # 项目的所有社交账号
    socials = scrapy.Field()


