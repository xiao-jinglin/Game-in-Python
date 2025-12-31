import pygame
from os.path import join

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

player_surf = pygame.image.load(join("Game-in-Python", "images", "player_ship.png"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((50, 50, 50))
    screen.blit(player_surf, (WIDTH / 2 - 50, HEIGHT -150))
    pygame.display.update()

pygame.quit()