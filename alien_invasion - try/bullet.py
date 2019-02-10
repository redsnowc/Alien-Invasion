import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射字典管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示字典的矩形，再正确设置其位置
        self.image = ai_settings.bullet_image
        self.rect = ai_settings.bullet_image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)


        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self, ai_settings):
        """在屏幕上绘制子弹"""
        self.screen.blit(self.image, self.rect)
