import pygame
import time
import random

from colorClass import Color
from snakeClass import Snake
from windowClass import Window
from fruitClass import Fruit

# Call the classes
s = Snake()
c = Color()
w = Window()
f = Fruit()

# Choose your option

c.SnakeColor()

w.chooseSizeScreen()

s.chooseSpeed()

# Start the game window
w.screenWidth()


fps = pygame.time.Clock()

score = 0

while True:

    # How the snake moves
    s.snakeMovement()

    # If the snake is on the fruit it grows and the fruit change position
    s.snake_body.insert(0, list(s.snake_position))
    if s.snake_position[0] == f.fruit_position[0] and s.snake_position[1] == f.fruit_position[1]:
        score += 10

        # pygame.time.set_timer(my_event, 1000)
        f.fruit_spawn = False

    else:
        s.snake_body.pop()
        # pygame.time.set_timer(my_event, 0)


    if not f.fruit_spawn:
        f.fruit_position = [random.randrange(1, (w.screen_x // 10)) * 10,
                          random.randrange(1, (w.screen_y // 10)) * 10]



    f.fruit_spawn = True

    # Have to refresh with white otherwise the snake keep growing
    w.game_window.fill(c.white)

    # Lines background (like a notebook)
    w.linesBg()


    for loc in s.snake_body:
        pygame.draw.rect(w.game_window, c.snakecolor,
                         pygame.Rect(loc[0], loc[1], 10, 10))
    pygame.draw.rect(w.game_window, c.red, pygame.Rect(
        f.fruit_position[0], f.fruit_position[1], 10, 10))




    # Game Over if :
    if s.snake_position[0] < 0 or s.snake_position[0] > w.screen_x - 10:
        w.gameOver()
    if s.snake_position[1] < 0 or s.snake_position[1] > w.screen_y - 10:
        w.gameOver()


    for pixel in s.snake_body[1:]:
        if s.snake_position[0] == pixel[0] and s.snake_position[1] == pixel[1]:
            w.gameOver()




    # Refresh game screen
    pygame.display.update()

    # Frame Per Second
    fps.tick(s.snake_speed)
