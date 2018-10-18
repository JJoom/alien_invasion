import sys

import pygame

from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按下"""
    if event.key == pygame.K_q:
        sys.exit();
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)



def check_keyup_event(event,ship):
    """响应键盘弹起"""
    if event.key == pygame.K_RIGHT:
        # 停止移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def update_screen(ai_settings,screen,ship,bullets,alien):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    alien.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_setting,screen,ship,bullets):
    """如果子弹没有达到上限，就发射一颗子弹"""

    if len(bullets) < ai_setting.bullet_allowed:

        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)

