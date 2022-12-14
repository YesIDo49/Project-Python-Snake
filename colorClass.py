import pygame

class Color:
    def __init__(self):
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.pink = pygame.Color(255, 192, 203)
        self.yellow = pygame.Color(255, 255, 0)
        self.orange = pygame.Color(241, 90, 34)
        self.gray = pygame.Color(229, 229, 229)

        self.snakecolor = 0

    def SnakeColor(self):

        self.snakechoice = int(input("Choose snake color : blue (1), red (2), green (3), pink (4), "
                                     "yellow (5), orange (6) : "))

        if (self.snakechoice == 1):
            self.snakecolor = self.blue

        elif (self.snakechoice == 2):
            self.snakecolor = self.red

        elif (self.snakechoice == 3):
            self.snakecolor = self.green

        elif (self.snakechoice == 4):
            self.snakecolor = self.pink

        elif (self.snakechoice == 5):
            self.snakecolor = self.yellow

        elif (self.snakechoice == 6):
            self.snakecolor = self.orange

        else:
            print("Wrong choice !")
            self.SnakeColor()

