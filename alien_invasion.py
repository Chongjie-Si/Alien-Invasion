from settings import Settings
from ship import Ship
from button import Button
import game_functions as gf
import pygame
from pygame.sprite import Group
from game_stats import GameStat
from scoreboard import Scoreboard


def run_game():

    pygame.init()
    pygame.display.set_caption('Alien Invasion')
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStat(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_event(ai_settings, screen, stats, sb, play_button, aliens, ship, bullets)
       # if stats.game_active:
        ship.upgrade()
        gf.upgrade_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.upgrade_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            # 创建外星人群


run_game()
