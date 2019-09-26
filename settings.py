# Ryan Chen
# 893219394
# Implementation of the settings class, which maintains various static and dynamic varibles

class Settings:
    # This class stores all settings for Alien Invasion

    def __init__(self):
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_width = 64
        self.ship_height = 64
        self.ship_move_left = False
        self.ship_move_right = False
        self.ship_speed = 2
        self.ship_lives = 3

        # Alien settings
        self.alien_width = 64
        self.alien_height = 64
        self.alien_speed = 1
        self.alien_points = 50

        # Fleet settings
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255, 255, 255)
        self.bullet_max = 3

        self.speedup_amount = 2

    def init_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 10
        self.alien_speed = 3
        self.alien_points = 50

    def speedup(self):
        self.ship_speed += self.speedup_amount
        self.bullet_speed += self.speedup_amount
        self.alien_speed += self.speedup_amount
        self.alien_points *= self.speedup_amount


