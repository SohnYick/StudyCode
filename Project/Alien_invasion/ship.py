import pygame

class Ship:
    """ 飞船类 """

    def __init__(self,ai_game):
        """ 初始化飞船并设置其初始位置 """

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings= ai_game.settings

        # 加载飞船的图像
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 每艘新的飞船，都位于屏幕底部居中
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标记
        self.moving_right = False
        self.moving_left = False

        # 飞船开始位置转为浮点数
        self.x = float(self.rect.x)

    def update(self):
        
        # 更新飞船位置，而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # 根据飞船位置，更新rect对象
        self.rect.x = self.x

    def blitme(self):
       """ 在指定位置绘制飞船 """ 
       self.screen.blit(self.image,self.rect)
