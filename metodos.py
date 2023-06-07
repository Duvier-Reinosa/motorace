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

def creditsGame(screen):
    pygame.display.set_caption("Credits")
    font = pygame.font.Font(None, 36)  # Fuente para el texto
    font2 = pygame.font.Font(None, 20)  # Fuente para el texto
    background = pygame.image.load("assets/calle.png")

    out = True
    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out = False
            
        screen.blit(background, (0, 0))

        text1 = font.render("Credits", True, (0, 0, 0))
        audio = font2.render("Audio from Youtube", True, (0, 0, 0))
        image = font2.render("Pictures from Freepick, opengameart", True, (0, 0, 0))

        screen.blit(text1, (105, 50))
        screen.blit(audio, (105, 100))
        screen.blit(image, (105, 130))


        pygame.display.flip()
        

def initGame(screen):
    pygame.display.set_caption("Moto Race")

    font = pygame.font.Font(None, 36)  # Fuente para el texto
    background = pygame.image.load("assets/calle.png")
    playButton = pygame.image.load("assets/playButton.png")
    creditsButton = pygame.image.load("assets/creditsButton.png")

    out = True
    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= 130 and mouse[0] <= 340 and mouse[1] >= 200 and mouse[1] <= 300:
                    out = False
                if mouse[0] >= 130 and mouse[0] <= 340 and mouse[1] >= 300 and mouse[1] <= 400:
                    creditsGame(screen)

        screen.blit(background, (0, 0))
        screen.blit(playButton, (130, 200))
        screen.blit(creditsButton, (130, 300))

        text1 = font.render("Welcome to Moto Race", True, (0, 0, 0))

        screen.blit(text1, (105, 50))


        pygame.display.flip()



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
