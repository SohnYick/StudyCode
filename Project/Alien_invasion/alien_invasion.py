import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    
    def __init__(self):

        # 导入配置        
        self.settings = Settings() 

        pygame.init()

        # 实例窗口，并设置宽高
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # 窗口标题
        pygame.display.set_caption(self.settings.title)
        # 窗口背景色
        self.bg_color = self.settings.bg_color 

        # 飞船
        self.ship = Ship(self)
        # 飞船的子弹
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ 游戏的主循环 """
        while True:
            
            # 事件监听
            self._check_events()

            # 飞船更新
            self.ship.update()

            # 子弹更新
            self._update_bullets()

            # 屏幕更新：重绘
            self._update_screen()
            
    def _check_events(self):
        """ 事件监听 """

        # 辨别出事件的类型
        for event in pygame.event.get():
            # 点击X退出游戏（全屏模式下，关闭按钮不可见）
            if event.type == pygame.QUIT:
                sys.exit()
            # 按钮按下事件
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 按钮弹起事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    

    def _check_keydown_events(self,event):
        """ 按键按下检测 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self._fire_bullet()
        # 按q退出游戏
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """ 按键松开检测 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ 创建一颗子弹，并放入编组的bullets编组中 """

        # 屏幕上存在的子弹数量有限
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):

        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)

        # 绘制飞船
        self.ship.blitme()

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_bullets(self):

        self.bullets.update()
        
        # 删除超出屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":

    AlienInvasion().run_game()
