import scrapy

from CrawlPad.items import CrawlpadItem

class BscpadSpider(scrapy.Spider):
    name = 'bscpad'
    allowed_domains = ['bscpad.com']
    start_urls = ['http://bscpad.com/projects']

    def parse(self, response):
        selector = response.selector
        # 查询页面中所有项目的html
        projects = selector.css("div.single-item")
        # 遍历所有项目，从中提取所需的信息
        for project in projects:
            # 单个项目的所有信息会封装成一个Item
            item = CrawlpadItem()
            # 解析所有信息（字符串形式）。
            item["title"] = project.css("div.title-box h3 div::text").extract_first()
            item["short_desc"] = project.css("div.item-short-desc::text").extract_first()
            # 解析出社交地址
            item["socials"] = {
                "index" : project.css("div.item-social>a::attr(href)").extract_first(),
                "twitter" : project.css("div.item-social a[href*=twitter]::attr(href)").extract_first(),
                "medium" : project.css("div.item-social a[href*=medium]::attr(href)").extract_first(),
                "telegram" : project.css("div.item-social a[href*='t.me']::attr(href)").extract_first()
            }
            # 传递给Pipeline处理
            yield item
