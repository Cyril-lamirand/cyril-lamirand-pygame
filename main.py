import pygame
import math
# Classes
from game import Game
pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Cyril LAMIRAND - Shooter")
screen = pygame.display.set_mode((1080, 720))
# Gestion du fond d'écran du jeu
background = pygame.image.load("assets/bg.jpg")

# Charger la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


running = True

game = Game()

# Boucle d'exécution du jeu
while running:

    # Appliquer l'image de fond du jeu
    screen.blit(background, (0, -200))

    # Vérifier si le jeu à commencer ou non
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mettre à jour la fenêtre du jeu
    pygame.display.flip()

    # Fermer la fenêtre de jeu
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu...")
        # Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.lauch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


