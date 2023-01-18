import time

import requests

from spider import BookSpider

if __name__ == "__main__":

    start = time.time()

    spider = BookSpider()
    pages = spider.craw()
    for page in pages:
        print(page["url"],len(page["html"]))

    end = time.time()
    print(f"用时：{end-start}")


