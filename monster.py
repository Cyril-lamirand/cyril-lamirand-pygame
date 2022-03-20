import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 1
        self.start_animation()

    def update_animation(self):
        self.animate(loop = True)

    def damage(self, amount):
        self.health -= amount

        # Vérifier si le monstre est mort
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 3)

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


