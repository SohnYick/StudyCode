import random

class Car:

	def __init__(self, make, model, year):
		"""
		根据制造商、型号、生产年份实例化一辆汽车
		"""
		self.make = make
		self.model = model
		self.year = year
		# 里程
		self.odometer = 0
		# 油箱容量
		self.tank_size = 100


	def get_fullname(self):
		"""
		获取汽车的全名
		"""
		return f"{self.year} {self.make} {self.model}"

	def get_odometer(self):
		"""
		:return: 返回汽车奔跑里程数
		"""
		return self.odometer

	def get_tank(self):
		"""
		:return: 返回汽车的油箱容量
		"""
		return self.tank_size

	def update_odometer(self,miles):
		"""
		更新汽车里程。
		"""
		# 防止里程回调
		if miles < self.odometer:
			print("警告：里程不能回调。")
			return
		self.odometer = miles

	def increament_odometer(self,miles):
		"""
		增加汽车里程。
		汽车奔跑时会使用。
		"""
		if miles < 0:
			print(f"警告：里程增量不能为负数：{self.odometer}")
			return
		self.odometer += miles

class ElectricCar(Car):

	def __init__(self, make, model, year):

		# 调用父类的构造方法 —— 初始化父类的属性
		super().__init__(make,model,year)

		# 免费配送的电容
		self.battery = Battery()

	def run(self,day_number):
		"""
		让电动车跑起来
		:day_number: 奔跑的天数
		:return: 返回行驶的共计公里数
		"""
		# 共计的公里数量
		count_number = 0
		# 奔跑的天数
		count_day = 0
		for n in range(day_number):

			# 每天奔跑的公里数，10公里以内
			number = random.randint(1,10)

			# 只有先消耗了电量，车才能跑起来，里程才能增加
			# 消耗电容的电，设：1公里消耗1的电容量
			is_run = self.battery.consume(number)

			# 如果电容没电，无法奔跑，循环直接结束
			if is_run is False:
				# 电容可能还有电量，但是不足当天用量。
				# 所以需要把这最后电量，在最后一天消耗完后，才能退出循环。 ！！！ 问题遗留
				# - 最好让self.battery.consume(number)返回负数、零、正数（而非Bool），分别表示三种情况：
				# - 正数：汽车可以奔跑。返回值为剩余电量。
				# - 零：汽车可以奔跑。表示汽车内的电容已经为空。
				# - 负数：汽车无法奔跑。返回值表示差的电量。

				count_day = n
				break
			# 共计每天的奔跑公里
			count_number += number
			# 增加里程数，设：1公里增加1的里程数
			super().increament_odometer(number)
			# 打印今日奔跑距离
			print(f"第{n+1}天汽车行驶了{number}里")

		# 打印共计奔跑距离
		print(f"汽车 {self.get_fullname()} 在 {n} 天里跑了 {count_number} 公里。")
		
	def showInfo(self):
		"""
		展示汽车信息
		"""
		print("汽车信息如下：")
		print(f"全名：{self.get_fullname()}")
		print(f"里程：{self.get_odometer()}")
		print(f"电容：{self.get_battery().get_max()}")
		print(f"电量：{self.get_battery().get_now()}")
		print("\n")


	def get_tank(self):
		"""
		重写父类的get_tank方法，因为电动车是没有油箱的。
		"""
		print("电动车怎么会有邮箱呢？笨蛋。")


	def get_battery(self):
		return self.battery

	def set_battery(self,battery):
		"""
		更换电容
		"""
		self.battery = battery

	def get_endurance(self):
		"""
		得知汽车还能跑多久
		:return: 返回可续航的公里数
		"""
		# 假设每1的电量可跑1公里
		return self.battery.get_now * 1


class Battery:
	"""
	电动车的电容
	"""
	def __init__(self,size = 75):

		# 最大电容量
		self.max = size
		# 默认，新电容是满电
		self.now = size
	
	def charge(self,number):
		"""
		电容充电
		:number: 要充的电量
		"""

		# 当前电量+要充电量 大于 最大电容量
		if self.now+number > self.max:
			# 给出提示消息
			print("电已经充满!")
			print(f"- 最大电容量为{self.max}")
			print(f"- 当前电量为{self.now}")
			print(f"- 要充的电量为{number}")
			print(f"- 电容无法达到{self.now+number}")
			# 直接将当前电量设置为最大电容量
			self.now = self.max
			return
		self.now += number

	def consume(self,number):
		"""
		消耗电容的电
		:number: 消耗的电量
		:return: 电容没电返回False
		"""

		# 当前电量 小于 需要消耗的电量
		if self.now < number:
			# 发出警告，结束方法的执行，返回False。
			print(f"警告：你的电容已经没有电啦！")
			return False

		self.now -= number
		return True


	def get_max(self):
		"""
		:return: 返回最大电容量
		"""
		return self.max

	def get_now(self):
		"""
		:return: 返回当前电量
		"""
		return self.now

