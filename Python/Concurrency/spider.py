import requests
import pyquery 

class BookSpider:
    """ 本类爬取豆瓣读书 """

    def __init__(self,tag="编程",page_number=5):
        """
        根据给定的标签和要爬取的页数，构造一个对象。
        :param tag: 标签（默认：编程）
        :param tag: 页数（默认：5）
        """
        self.urls = [
            f"https://book.douban.com/tag/{tag}?start={(page-1)*20}&type=t"
            for page in range(1,page_number+1)
        ]

        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
        }

    def parse():
        """
        """


    def craw_html(self,url):
        """
        抓取给定URL的HTML
        """
        return requests.get(url=url,headers=self.headers).text


