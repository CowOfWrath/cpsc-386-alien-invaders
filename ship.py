# Ryan Chen
# 893219394
# Implementation of the ship class

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, width, height):
        # Initialize ship and start position
        super(Ship, self).__init__()
        self.screen = screen

        self.image = pygame.transform.scale(pygame.image.load("Images/ship.png"), (width, height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, settings):
        if settings.ship_move_right and self.rect.right < settings.screen_width:
            self.rect.centerx += 1 * settings.ship_speed
        elif settings.ship_move_left and self.rect.left > 0:
            self.rect.centerx -= 1 * settings.ship_speed
