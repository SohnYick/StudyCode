import threading
import time

import requests


if __name__ == "__main__":

    start = time.time()

    bs = BookSpider()

    # 线程的容器
    threads = []
    for url in bs.urls:
        threads.append(
            threading.Thread(target=bs.craw,args=(url,))
        )

    # 线程启动
    for thread in threads:
        thread.start()
    # 线程停止


    end = time.time()

    print(f"用时:{end-start}")


