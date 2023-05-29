import pygame
import time

pygame.init()
sizeScreen = (470,600)
screen = pygame.display.set_mode(sizeScreen)

pygame.display.set_caption("Moto Race")

clock = pygame.time.Clock()
fps = 60

background = pygame.image.load("assets/calle.png")
backgroundPosition = 0


play = True
while play:

    
    # se captura los eventos y se ejecutan sus funciones
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

    backgroundPosition += 2  # Velocidad de desplazamiento

    # Dibujar fondo
    screen.blit(background, (0, backgroundPosition))
    screen.blit(background, (0, backgroundPosition - sizeScreen[1]))

    if backgroundPosition >= sizeScreen[1]:
        backgroundPosition = 0

    pygame.display.flip()
    clock.tick(fps)
