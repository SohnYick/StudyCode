"""
能源模块，为各种汽车提供各种动力能源。
"""

class Energy:
	"""
	能源容器类
	"""
	def __init__(self,max):
		"""
		max:能源容器的容量
		"""
		# 保证容量最小为1
		if max <= 0:
			print(f"容量最小为1，不能为{max}。")
			max = 1
		self.max = max

		# 当前能源等于容量 —— 满能量
		self.now = self.max

	def set_now(self,number):
		# 设置的能量不能小于0 —— 不能为负数
		# 设置的能量不能大于最大容量
		if number < 0:
			print("设置的能量值不能小于0")
		elif number > self.max: 
			print("设置的能量值不能大于容量")
		else:
			self.now = number

	def get_now(self):
		return self.now

	def get_max(self):
		return self.max



class Battery(Energy):
	"""
	电瓶类，供电动汽车使用
	"""


class Tank(Energy):
	"""
	油箱类，供油箱汽车使用
	"""

if __name__ = "__main__":
	
	