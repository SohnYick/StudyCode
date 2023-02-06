import threading

lock = threading.Lock()

class Account:
    def __init__(self,balance):
        self.balance = balance
    
    def took(self,amount):
        with lock:
            if self.balance > amount:
                print("余额足够")
                self.balance -= amount
                print("取钱成功")
            else:
                print("余额不足，取钱失败！")
    
my_account = Account(1000)

t1 = threading.Thread(target=my_account.took,args=(800,))
t2 = threading.Thread(target=my_account.took,args=(800,))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"账户余额为：{my_account.balance}")