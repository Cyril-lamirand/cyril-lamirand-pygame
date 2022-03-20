import pygame
from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent

class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # Appliquer le joueur dans la fenêtre
        screen.blit(self.player.image, self.player.rect)

        # Afficher / Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Barre de l'event Comet
        self.comet_event.update_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Faire avancer les monstres vers le joueur
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Faire tomber les comettes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Dessiner le projectile
        self.player.all_projectiles.draw(screen)

        # Dessiner les monstres
        self.all_monsters.draw(screen)

        # Dessiner les cometes
        self.comet_event.all_comets.draw(screen)

        # Vérifier si le joueur veut se déplacer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))


