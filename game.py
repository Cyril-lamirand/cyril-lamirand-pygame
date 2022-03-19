import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # Appliquer le joueur dans la fenêtre
        screen.blit(self.player.image, self.player.rect)

        # Afficher / Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Faire avancer les monstres vers le joueur
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Dessiner le projectile
        self.player.all_projectiles.draw(screen)

        # Dessiner les monstres
        self.all_monsters.draw(screen)

        # Vérifier si le joueur veut se déplacer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))


