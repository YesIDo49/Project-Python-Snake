import pygame
import time

from colorClass import Color

c = Color()


class Window:
    def __init__(self):
        # Window size
        self.screen_x = 100
        self.screen_y = 100
        self.game_window = 0


    def chooseSizeScreen(self):
        self.screenchoice = int(input("Choose screen size : small (1), medium (2), large (3): "))

        if (self.screenchoice == 1):
            self.screen_x = 400
            self.screen_y = 150

        elif (self.screenchoice == 2):
            self.screen_x = 700
            self.screen_y = 460

        elif (self.screenchoice == 3):
            self.screen_x = 1020
            self.screen_y = 720

        else:
            print("Wrong choice !")
            self.chooseSizeScreen()

    def screenWidth(self):
        self.game_window = pygame.display.set_mode((self.screen_x, self.screen_y))
        pygame.init()


    # game over function
    def gameOver(self):


        # after 1 seconds we will quit the program
        time.sleep(1)

        # deactivating pygame library
        pygame.quit()

        # quit the program
        quit()

    def linesBg(self):
        i = 0

        while i <= self.screen_y:
            pygame.draw.lines(self.game_window, c.gray, True, [(0, i), (self.screen_x, i)])
            i += 10

        j = 0

        while j <= self.screen_x:
            pygame.draw.lines(self.game_window, c.gray, True, [(j, 0), (j, self.screen_y)])
            j += 10



