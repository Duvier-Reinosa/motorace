import pygame
import time
import random

pygame.init()
sizeScreen = (470, 600)
screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption("Moto Race")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Fuente para el texto

background = pygame.image.load("assets/calle.png")
carBlue = pygame.image.load("assets/carBlue.png")
carGreen = pygame.image.load("assets/carGreen.png")
carRed = pygame.image.load("assets/carRed.png")
carRose = pygame.image.load("assets/carRose.png")
carYellow = pygame.image.load("assets/carYellow.png")

# assets

# imgs
moto = pygame.image.load("assets/moto.png")
motoScaled = pygame.transform.scale(moto, (40, 90))

# sounds

# general variables
backgroundPosition = 0
fps = 60
xMoto = 180
yMoto = 480
velocidadMovXMoto = 0
velocidadMovYMoto = 0
initialTime = pygame.time.get_ticks()
velocityGame = 2

# Lista de posiciones de los carros
carPositions = []

# Función para agregar un nuevo carro a la lista
def addCar():
    lane = random.randint(0, 1)  # Selección aleatoria de un carril
    xPos = 170 + lane * 60  # Posición X según el carril seleccionado
    yPos = -100 * (len(carPositions) * 3)   # Empieza arriba de la pantalla la operación funciona para poner más separados los carros en la pantalla
    carPositions.append((xPos, yPos, selectCar(random.randint(0, 4))))  # Agregar el carro a la lista

# Función para mover los carros y comprobar colisiones
def updateCars():
    for i, (x, y, car) in enumerate(carPositions):
        y += velocityGame  # Velocidad de movimiento del carro
        carPositions[i] = (x, y, car)  # Actualizar posición del carro

        # Eliminar carros que hayan salido de la pantalla
        if y > 600:
            carPositions.pop(i)

def selectCar(position):
    if position == 0:
        return carBlue
    elif position == 1:
        return carGreen
    elif position == 2:
        return carRed
    elif position == 3:
        return carRose
    elif position == 4:
        return carYellow
    else:
        return carBlue

# Bucle principal del juego
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidadMovXMoto += -5
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

    backgroundPosition += velocityGame  # Velocidad de desplazamiento

    # Actualización de la posición de la moto con reglas para no salirse de la carretera
    xMoto += velocidadMovXMoto
    if xMoto <= 179 or xMoto >= 245:
        xMoto -= velocidadMovXMoto
        velocidadMovXMoto = 0

    yMoto += velocidadMovYMoto
    if yMoto >= 480 or yMoto <= 2:
        yMoto -= velocidadMovYMoto
        velocidadMovYMoto = 0

    # Dibujar fondo
    screen.blit(background, (0, backgroundPosition))
    screen.blit(background, (0, backgroundPosition - sizeScreen[1]))

    # Dibujar carros
    for (x, y, car) in carPositions:
        screen.blit(car, (x, y))

    # mostrar moto
    screen.blit(motoScaled, (xMoto, yMoto))

    # Calcular el tiempo transcurrido
    currentTime = pygame.time.get_ticks() - initialTime

    # Formatear el tiempo en segundos
    currentSeconds = currentTime // 1000

    # Crear el texto
    textTime = font.render("Time: " + str(currentSeconds) + " sec", True, (0, 0, 0))

    # Mostrar el texto en la pantalla
    screen.blit(textTime, (10, 10))

    # Generar nuevos carros aleatoriamente
    if random.random() < 0.01:  # Probabilidad de generar un nuevo carro en cada iteración
        addCar()

    # Actualizar posición de los carros y comprobar colisiones
    updateCars()

    if backgroundPosition >= sizeScreen[1]:
        backgroundPosition = 0

    pygame.display.flip()
    clock.tick(fps)
