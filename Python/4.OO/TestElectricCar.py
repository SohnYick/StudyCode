from classes import ElectricCar

if __name__ == "__main__":

	my_car = ElectricCar("特斯拉","C31",2020)

	my_car.showInfo()

	# 让汽车跑20天
	my_car.run(20)
	my_car.showInfo()

	# 给汽车100的电
	my_car.get_battery().charge(100)
	my_car.showInfo()

	# 再让汽车跑
	my_car.run(10)
	my_car.showInfo()
