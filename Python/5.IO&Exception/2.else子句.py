
if __name__ == "__main__":

	print("本程序可以帮你做两数除法运算。")
	print("输入q退出程序。","\n")

	while True:
		first_number = input("请输入被除的数字：")
		if first_number == "q":
			break			
		second_number = input("请输入除数：")
		if second_number == "q":
			break
		try:
			answer = int(first_number)/int(second_number)
		except ZeroDivisionError:
			print("除数不能为零。")
		else:
			print(f"结果为{answer}")



	