import pygame
from time import sleep
from threading import Timer
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

converted_score = str(score)

score_text = 'Score : ', type(converted_score)

font = pygame.font.Font('freesansbold.ttf', 16)

text = font.render('Score : ' + str(score), True, c.black)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (w.screen_x // 2, 10)

delay = 3
getTicksLastFrame = 0

timer = 0


while True:

    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timer += deltaTime

    if timer > 10:
        f.fruit_appear = False
        timer = 0

    # How the snake moves
    s.snakeMovement()

    # If the snake is on the fruit it grows and the fruit change position
    s.snake_body.insert(0, list(s.snake_position))
    if s.snake_position[0] == f.fruit_position[0] and s.snake_position[1] == f.fruit_position[1]:
        score += 10

        # pygame.time.set_timer(my_event, 1000)
        f.fruit_appear = False
        timer = 0


    else:
        s.snake_body.pop()


    if not f.fruit_appear:
        f.fruit_position = [random.randrange(1, (w.screen_x // 10)) * 10,
                          random.randrange(1, (w.screen_y // 10)) * 10]


    f.fruit_appear = True



    # Have to refresh with white otherwise the snake keep growing
    w.game_window.fill(c.white)

    # Lines background (like a notebook)
    w.linesBg()


    # Score show
    w.game_window.blit(text, textRect)



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

    text = font.render('Score : ' + str(score), True, c.black)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (w.screen_x // 2, 10)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second
    fps.tick(s.snake_speed)

