import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    
    def __init__(self):
        
        self.settings = Settings() 

        pygame.init()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # 窗口的标题
        pygame.display.set_caption(self.settings.title)
        
        # 背景颜色
        self.bg_color = self.settings.bg_color 

        # 飞船
        self.ship = Ship(self)

    def run_game(self):
        """ 游戏的主循环 """
        while True:
            
            self._check_events()

            self.ship.update()

            self._update_screen()
            
    def _check_events(self):
        """ 按键和鼠标事件 """
        for event in pygame.event.get():

            # 全屏模式下，关闭按钮不可见
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self,event):
        """ 按键按下 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按q退出游戏
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """ 按键松开 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):

            # 每次循环都重绘屏幕
            self.screen.fill(self.bg_color)

            # 绘制飞船
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":

    ai = AlienInvasion()
    ai.run_game()
