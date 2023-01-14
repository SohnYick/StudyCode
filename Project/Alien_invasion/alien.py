import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 表示单个外星人 """

    def __init__(self,ai_game):
        """ 初始化外星人的位置 """
        super().__init__()
        self.screen = ai_game.screen

        # 加载图形，并设置其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
