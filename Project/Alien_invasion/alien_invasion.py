import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stats import Stats

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

        # 记录游戏信息
        self.stats = Stats(self)

        # 飞船
        self.ship = Ship(self)
        # 存储所有飞船子弹的编组 
        self.bullets = pygame.sprite.Group()

        # 存储外星人舰队的编组
        self.aliens = pygame.sprite.Group()
        # 创建外星人舰队
        self._create_fleet()
        

    def run_game(self):
        """ 游戏的主循环 """
        while True:
            
            # 事件监听
            self._check_events()

            # 这些部分，只有游戏处于激活状态才会运行
            if self.stats.game_active:
                # 飞船更新
                self.ship.update()
                # 子弹更新
                self._update_bullets()
                # 外星人更新
                self._update_aliens()

            # 屏幕更新：重绘
            self._update_screen()

    def _ship_hit(self):
        """ 响应飞船被外星人撞到 """

        # 如果还有飞船
        if self.stats.ship_limit > 0:
            # 减少飞船数量
            self.stats.ship_limit -= 1
            # 清空子弹和外星人
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将新飞船放于底部中央
            self._create_fleet()
            self.ship.center_ship()
            # 游戏暂停
            sleep(0.5)
        else:
            # 没有飞船，改变将游戏的状态改变
            self.stats.game_active = False

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

        # 绘制外星人
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_bullets(self):

        self.bullets.update()
        
        # 删除超出屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


    def _check_bullet_alien_collisions(self):
        """ 检测子弹与外星人之间的碰撞，并做出相应动作 """

        # 检测子弹是否击中了外星人
        # 如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True
            )

        # 检测是否还有外星人存在。
        # 如果没有，删除所有屏幕中的子弹，并新创建一批外星人。
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人与飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测外星人是否达到屏幕底部
        self._check_aliens_bottom()

    def _create_fleet(self):
        """ 创建外星人舰队 """
        alien = Alien(self)
        self.aliens.add(alien)
       
        # 外星人的宽高
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        # 行和列的可用空间
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = self.settings.screen_height - (3 * alien_height) - self.ship.rect.height
        # 一行可以有多少个外星人
        alien_rows_number = available_space_x // (2 * alien_width)
        # 一共可以有多少行
        alien_cols_number = available_space_y // (2 * alien_height)

        # 创建外星人舰队
        for row_number in range(alien_cols_number):
            for col_number in range(alien_rows_number):
                self._create_alien(row_number,col_number)

    def _check_aliens_bottom(self):
        """ 检测是否有外星人到达屏幕底部 """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            # 如果飞船到达底部
            if alien.rect.bottom >= screen_rect.bottom:
                # 飞船跟被撞到一样
                self._ship_hit()
                break

    def _create_alien(self,row_number,col_number):
        """ 创建一个外星人"""
        alien = Alien(self)
        alien_width = alien.rect.width
        # 设置位置
        alien.x = alien_width + 2 * alien_width * col_number
        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        # 加入外星舰队编组
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ 有外星人达到边缘时，采取相应的措施 """
        for alien in self.aliens.sprites():
            if alien._check_edge():
                self._check_fleet_direction()
                break

    def _check_fleet_direction(self):
        """ 将整群外星人下移，并改变它们的方向 """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == "__main__":

    AlienInvasion().run_game()
