# Ryan Chen
# 893219394
# Implementation of the GameStats class which maintains part of the game state and score
class GameStats:

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.running = True
        self.active = False

    def reset_stats(self):
        self.ship_lives = self.settings.ship_lives
        self.score = 0
        self.high_score = 0
        self.level = 1