import requests
import time

class BookSpider:
    """ 本类爬取豆瓣读书上面的数据 """

    def __init__(self,tag="编程",page_number=5):
        """
        根据给定的标签和要爬取的页数，构造一个对象。
        :param tag: 标签
        :param tag: 页数
        """
        self.urls = [
            f"https://book.douban.com/tag/{tag}?start={(page-1)*20}&type=t"
            for page in range(1,page_number+1)
        ]

        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
        }

    def craw(self):
        """
        抓取数据
        :return: 返回字典数组，数组中每个字典包含网页相关的信息
        """
        pages = [] 
        for url in self.urls:
            pages.append({
                "url":url,
                "html":requests.get(url=url,headers=self.headers).text
            })
        return pages
            

if __name__ == "__main__":

    start = time.time()

    spider = BookSpider()
    pages = spider.craw()
    for page in pages:
        print(page["url"],len(page["html"]))

    end = time.time()
    print(f"用时：{end-start}")


