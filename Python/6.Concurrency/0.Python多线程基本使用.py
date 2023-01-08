import threading
import time

def function(number):
    # 假设函数执行需要2秒
    time.sleep(2)
    print(number,"执行完毕")

if __name__ == "__main__":

    start = time.time()
    # 创建10个线程，并加入容器
    threads = []
    for n in range(1,11):
        threads.append(
            threading.Thread(target=function,args=(n,))
        )
    # 线程启动
    for thread in threads:
        thread.start()
    # 线程等待停止
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"执行消耗时间：{end-start}")