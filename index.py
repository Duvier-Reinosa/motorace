import pygame
import time

pygame.init()
sizeScreen = (470,600)
screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption("Moto Race")


clock = pygame.time.Clock()

background = pygame.image.load("assets/calle.png")

#assets

# imgs
moto = pygame.image.load("assets/moto.png")
motoScaled = pygame.transform.scale(moto, (50, 100))

# sounds

# general variables
backgroundPosition = 0
fps = 60
xMoto = 180
yMoto = 480
velocidadMovXMoto = 0
velocidadMovYMoto = 0


play = True
while play:

    
    # se captura los eventos y se ejecutan sus funciones
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidadMovXMoto += - 5
                if event.key == pygame.K_RIGHT:
                    velocidadMovXMoto += 5
                if event.key == pygame.K_UP: 
                    velocidadMovYMoto = -5
                if event.key == pygame.K_DOWN:
                    velocidadMovYMoto = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    velocidadMovXMoto = 0
                if event.key == pygame.K_RIGHT:
                    velocidadMovXMoto = 0
                if event.key == pygame.K_UP:
                    velocidadMovYMoto = 0
                if event.key == pygame.K_DOWN:
                    velocidadMovYMoto = 0

    backgroundPosition += 2  # Velocidad de desplazamiento
    # Actualización de la posición de la moto
    xMoto += velocidadMovXMoto 
    yMoto += velocidadMovYMoto 

    # Dibujar fondo
    screen.blit(background, (0, backgroundPosition))
    screen.blit(background, (0, backgroundPosition - sizeScreen[1]))
    

    # mostrar moto
    screen.blit(motoScaled, (xMoto, yMoto))

    if backgroundPosition >= sizeScreen[1]:
        backgroundPosition = 0

    pygame.display.flip()
    clock.tick(fps)
