import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" 飞船所发射的子弹 """

	def __init__(self,ai_game):
		""" 在飞船的前方创建一个子弹 """

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# 在 0,0 除创建一颗子弹
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		# 设置到正确的位置（飞船之前）
		self.rect.midtop = ai_game.ship.rect.midtop

		# 用小数表示子弹的位置
		self.y = float(self.rect.y)

	def update(self):
		"""
		更新子弹的状态
		"""

		# 表示子弹位置的小数值
		self.y -= self.settings.bullet_speed

		# 子弹的rect位置
		self.rect.y = self.y

	def draw_bullet(self):
		"""
		在屏幕上绘制子弹
		"""

		pygame.draw.rect(self.screen,self.color,self.rect)