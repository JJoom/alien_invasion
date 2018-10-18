import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    #初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen=screen,ai_settings=ai_settings)


    #创建一个用于存储子弹的编组
    bullets = Group()


    #创建一个外星人
    alien = Alien(ai_settings=ai_settings,screen=screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.top <= 0:
                bullets.remove(bullet)
        # 刷新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets,alien)

run_game()
