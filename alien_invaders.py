# Ryan Chen
# 893219394
# Implementation of the initialization and game loop

import pygame
import sys
import time
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
import game_functions as gf



def run():
    # Initialization
    pygame.init()
    settings = Settings()
    stats = GameStats(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(settings, screen, "Play")
    bg_color = settings.bg_color

    sb = Scoreboard(settings, screen, stats)




    ship = Ship(screen, settings.ship_width, settings.ship_height)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, aliens)

    clock = pygame.time.Clock()

    # Game loop
    running = True
    while stats.running:
        clock.tick(60)
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.active:
            ship.update(settings)
            gf.update_bullets(settings, screen, stats, sb, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        # Draw objects
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)



    sys.exit()


run()
