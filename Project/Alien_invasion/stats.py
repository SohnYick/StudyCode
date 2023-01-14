
class Stats:
	""" 游戏内的信息 """

	def __init__(self,ai_game):

		self.settings = ai_game.settings
		self.reset_stats()

		# 游戏刚刚开始，游戏状态处于激活
		self.game_active = True

	def reset_stats(self):
		""" 重置游戏信息：玩家重写开始游戏时会用得到 """
		self.ship_limit = self.settings.ship_limit