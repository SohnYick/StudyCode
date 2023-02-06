from classes import Car


def showInfo(car):
	print(f"我的新车是{car.get_fullname()}")
	print(f"它的里程是{car.get_odometer()}")
	print(f"它的油箱容量是{car.get_tank()}")
	print("--------------")

if __name__ == "__main__":

	my_car = Car("奥迪","A8",2000)

	# 汽车基本信息
	showInfo(my_car)

	# 汽车厂商设置初始里程
	my_car.update_odometer(15)
	# 汽车自己奔跑
	my_car.increament_odometer(20)
	showInfo(my_car)

	# 视图调回里程 或 增加不合理的里程，会报错
	my_car.update_odometer(5)
	my_car.increament_odometer(-2)
	