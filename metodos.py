import pickle
import pygame


def writeTimes(list):
    with open("db.pickle", "wb") as archivo:
        pickle.dump(list, archivo)
        

def readTimes():
    with open("db.pickle", "rb") as archivo:
        list = pickle.load(archivo)
        return list

def orderTimes(list):
    return sorted(list, reverse = True)


def endGame(time):
    pygame.init()
    sizeScreen = (470, 600)
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption("End Game")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)  # Fuente para el texto
    background = pygame.image.load("assets/calle.png")


    list = readTimes()
    list.append(time)
    list = orderTimes(list)
    writeTimes(list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))

        text1 = font.render("End Game", True, (0, 0, 0))
        text2 = font.render("The best 10 times", True, (0, 0, 0))
        text3 = font.render("Your time: " + str(time) + 'sec', True, (0, 0, 0))

        screen.blit(text1, (175, 10))
        screen.blit(text2, (135, 50))
        screen.blit(text3, (140, 80))

        for i in range(10):
            text = font.render(str(i + 1) + ". " + str(list[i]), True, (0, 0, 0))
            screen.blit(text, (200, 140 + i * 30))

        pygame.display.flip()
        clock.tick(60)


# endGame(5)
