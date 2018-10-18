import pygame
class Ship():
    """飞船的类"""

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        self.ai_settings = ai_settings
        #加载飞船图像并获取其外部矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕的底部中央
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    def update(self):
        """根据移动标志来调整飞船的位置"""

        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_top == True and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_bottom == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
