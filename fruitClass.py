import time
import random
import pygame

from windowClass import Window
w = Window()


class Fruit:
    def __init__(self):
        # fruit position
        self.fruit_position = [random.randrange(1, (w.screen_x // 10)) * 10,
                          random.randrange(1, (w.screen_y // 10)) * 10]

        self.fruit_spawn = True



