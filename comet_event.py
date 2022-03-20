import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 15):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):

        self.add_percent()

        pygame.draw.rect(surface, (0,0,0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])

