import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 表示单个外星人 """

    def __init__(self,ai_game):
        """ 初始化外星人的位置 """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载图形，并设置其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        """ 更新外星人的位置 """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def _check_edge(self):
        """ 检测外星人是否位于屏幕便于，如果是，就返回True """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True