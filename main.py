import pygame
# Classes
from game import Game
pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Cyril LAMIRAND - Shooter")
screen = pygame.display.set_mode((1080, 720))
# Gestion du fond d'écran du jeu
background = pygame.image.load("assets/bg.jpg")

running = True

game = Game()

# Boucle d'exécution du jeu
while running:

    # Appliquer l'image de fond du jeu
    screen.blit(background, (0, -200))

    # Appliquer le joueur dans la fenêtre
    screen.blit(game.player.image, game.player.rect)

    # Vérifier si le joueur veut se déplacer
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


