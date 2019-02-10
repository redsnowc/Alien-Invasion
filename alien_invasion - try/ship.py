import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = ai_settings.ship_image
        self.rect = ai_settings.ship_image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存小数点
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect，防止飞船移除屏幕外
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom

    def blitme(self, ai_settings):
        """在指定位置绘制飞船"""
        self.screen.blit(ai_settings.ship_image, self.rect)
