
if __name__ == "__main__":

	try:
		# 触发异常
		5/0
	except ZeroDivisionError:
		# 处理异常
		print("除数不能为零")