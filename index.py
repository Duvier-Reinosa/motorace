import pygame
import time
import random

pygame.init()
sizeScreen = (470, 600)
screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption("Moto Race")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Fuente para el texto


# assets

# imgs
background = pygame.image.load("assets/calle.png")

moto = pygame.image.load("assets/moto.png")
motoScaled = pygame.transform.scale(moto, (40, 90))

carBlue = pygame.image.load("assets/carBlue.png")
carGreen = pygame.image.load("assets/carGreen.png")
carRed = pygame.image.load("assets/carRed.png")
carRose = pygame.image.load("assets/carRose.png")
carYellow = pygame.image.load("assets/carYellow.png")

piston = pygame.image.load("assets/piston.png")
pistonScaled = pygame.transform.scale(piston, (40, 90))
tyre = pygame.image.load("assets/tyre.png")
tyreScaled = pygame.transform.scale(tyre, (60, 60))

# sounds

# general variables
backgroundPosition = 0
fps = 60
xMoto = 180
yMoto = 480
velocidadMovXMoto = 0
velocidadMovYMoto = 0
initialTime = pygame.time.get_ticks()
currentSeconds = 0
secondsToSubtract = 0
velocityGame = 2
powers = []
play = True
# Lista de posiciones de los Elementos(carros, llantas y pistones)
elementsPositions = []

# Función para agregar un nuevo elemento a la lista
def addElements():
    lane = random.randint(0, 1)  # Selección aleatoria de un carril
    xPos = 170 + lane * 60  # Posición X según el carril seleccionado
    yPos = -100 * (len(elementsPositions) * 3)   # Empieza arriba de la pantalla la operación funciona para poner más separados los elementos en la pantalla
    selectedElement = selectElements(random.randint(0, 6)) # Selección aleatoria de un elemento

    # Para centrar el piston el carril 
    if selectedElement == pistonScaled:
        xPos += 15

    elementsPositions.append((xPos, yPos, selectedElement))  # Agregar el elemento a la lista

# Función para mover los carros
def updateElements():
    for i, (x, y, element) in enumerate(elementsPositions):
        y += velocityGame  # Velocidad de movimiento del elemento
        elementsPositions[i] = (x, y, element)  # Actualizar posición del elemento

        # Eliminar elementos que hayan salido de la pantalla
        if y > 600:
            elementsPositions.pop(i)

def selectElements(position):
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
    if position == 5:
        return pistonScaled
    elif position == 6:
        return tyreScaled

# Bucle principal del juego
while play:
    # Calcular el tiempo transcurrido
    currentSeconds = pygame.time.get_ticks() - initialTime

    # Formatear el tiempo en segundos
    currentSeconds = currentSeconds // 1000

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
    if xMoto <= 179 or xMoto >= 255:
        xMoto -= velocidadMovXMoto
        velocidadMovXMoto = 0

    yMoto += velocidadMovYMoto
    if yMoto >= 480 or yMoto <= 2:
        yMoto -= velocidadMovYMoto
        velocidadMovYMoto = 0

    # Dibujar fondo
    screen.blit(background, (0, backgroundPosition))
    screen.blit(background, (0, backgroundPosition - sizeScreen[1]))

    # Dibujar elementos y controla colisiones
    for (x, y, element) in elementsPositions:
        elementDrawed = screen.blit(element, (x, y))
        # verificar colisiones
        if motoDrawed.colliderect(elementDrawed):
            if element == carBlue or element == carGreen or element == carRed or element == carRose or element == carYellow:
                play = False
            elif element == pistonScaled:
                powers.append(element)
                elementsPositions.remove((x, y, element))
            elif element == tyreScaled:
                secondsToSubtract += 5
                elementsPositions.remove((x, y, element))

    # Crear el texto
    textTime = font.render("Time: " + str(currentSeconds) + " sec", True, (0, 0, 0))
    textTime2 = font.render("To subtract: " + str(secondsToSubtract) + " sec", True, (0, 0, 0))
    textTime3 = font.render("Power:" + str(len(powers)), True, (0, 0, 0))

    # Mostrar el texto en la pantalla
    screen.blit(textTime, (10, 10))
    screen.blit(textTime2, (10, 40))
    screen.blit(textTime3, (10, 70))


    # mostrar moto
    motoDrawed = screen.blit(motoScaled, (xMoto, yMoto))


    # Generar nuevos carros aleatoriamente
    if random.random() < 0.01:  # Probabilidad de generar un nuevo carro en cada iteración
        addElements()

    # Actualizar posición de los elementos
    updateElements()

    if backgroundPosition >= sizeScreen[1]:
        backgroundPosition = 0

    pygame.display.flip()
    clock.tick(fps)
