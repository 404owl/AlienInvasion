import pygame
from pygame.sprite import Group

from interface.button import Button
import interface.game_functions as gf
from interface.game_stats import GameStats
from interface.settings import Settings
from interface.ship import Ship
from interface.scoreboard import Scoreboard


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    
    ai_settings=Settings()
    size=(ai_settings.screen_width,ai_settings.screen_height)
    #创建主屏幕
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("Alien Ivasion") 
    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")   
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()
    #创建外星人群
    gf.creat_fleet(ai_settings, screen, ship,aliens)
    #创建一个用于存储有系统及信息的实例，并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,sb,
                 aliens,bullets,stats,play_button)
        if stats.game_active:
            #刷新飞船
            ship.update()  
            #刷新子弹
            gf.update_bullets(ai_settings,screen,
                              ship,aliens,bullets,stats,sb) 
            #刷新外星人群
            gf.update_aliens(ai_settings,ship,
                             aliens,bullets,stats,screen,sb)     
            #刷新屏幕
        gf.update_screen(ai_settings,screen,ship,sb,
                         bullets,aliens,stats,play_button)
    

run_game()
