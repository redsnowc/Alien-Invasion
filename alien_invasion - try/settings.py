import pygame

class Settings():
    """储存游戏的所有设置"""

    def __init__(self):
        """初始化游戏静态设置"""
        # 屏幕设置
        self.screen_width = 798
        self.screen_height = 798
        self.bg_color = (135, 206, 250)
        self.background =  pygame.image.load(r'L:\python\alien_invasion\images\star.png')

        # 飞船设置
        self.ship_image = pygame.image.load(r'L:\python\alien_invasion\images\ship.png')
        self.ship_limit = 3

        # 子弹设置
        self.bullet_image = pygame.image.load(r'L:\python\alien_invasion\images\bullet.png')
        self.bullet_allowed = 20

        # 外星人设置
        self.alien_image = pygame.image.load(r'L:\python\alien_invasion\images\alien.png')
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船速度
        self.ship_speed_factor = 1.5
        # 子弹速度
        self.bullet_speed_factor = 3
        # 外星人速度
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
