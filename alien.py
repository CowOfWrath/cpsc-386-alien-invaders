# Ryan Chen
# 893219394
# Implementation of the Alien class

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, settings, screen, width, height):
        super(Alien, self).__init__()
        self.settings = settings
        self.screen = screen

        self.image = pygame.transform.scale(pygame.image.load("Images/alien.png"), (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #not sure if i want this
        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction

    def check_edges(self):
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True
