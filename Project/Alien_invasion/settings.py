class Settings:
    
    def __init__(self):
      
        # 窗口相关配置
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # 飞船相关配置
        self.ship_speed = 1
        self.ship_limit = 3 # 玩家的飞船数量
        
        # 子弹相关配置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # 外星人相关配置
        self.alien_speed = 1
        self.alien_drop_speed = 10
        # fleet_direction，1表示向右，-1表示向左
        self.fleet_direction = 1

