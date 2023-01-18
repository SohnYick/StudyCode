"""
汽车模块，模块中有各种各样的汽车。
"""
from energy import *

class Car:
	"""
	汽车，所有类型的汽车都有的功能和属性
	"""
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