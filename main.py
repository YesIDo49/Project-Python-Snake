import pygame
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
fruitPoint = 0

font = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 32)

#Delay variables
delay = 3
getTicksLastFrame = 0
timer = 0

#Countdown
clock = pygame.time.Clock()
countdown = 5
dt = 0

while True:

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    timer += deltaTime

    if timer > 5:
        f.fruit_appear = False
        timer = 0

    countdown -= dt
    if countdown <= 0:
        countdown = 5

    s.snakeMovement()

    # If the snake is on the fruit it grows and the fruit change position
    s.snake_body.insert(0, list(s.snake_position))
    if s.snake_position[0] == f.fruit_position[0] and s.snake_position[1] == f.fruit_position[1]:
        score += 10
        fruitPoint += 1
        f.fruit_appear = False
        timer = 0
        countdown = 5

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

    #Show Score
    scoreText = font.render('Score : ' + str(score), True, c.black)

    scoreRect = scoreText.get_rect()

    scoreRect.center = (w.screen_x // 2, 10)

    w.game_window.blit(scoreText, scoreRect)

    txt = font.render('Fruit reset : ' + str(int(countdown)), True, c.black)
    w.game_window.blit(txt, (w.screen_x // 2.3, 20))
    dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.

    for loc in s.snake_body:
        pygame.draw.rect(w.game_window, c.snakecolor,
                         pygame.Rect(loc[0], loc[1], 10, 10))
    pygame.draw.rect(w.game_window, c.red, pygame.Rect(
        f.fruit_position[0], f.fruit_position[1], 10, 10))

   #Game Over score
    gameOverText = font2.render('Final Score : ' + str(score) + ' | Total fruit : ' + str(fruitPoint), True, c.red)

    gameOverRect = gameOverText.get_rect()

    # set the center of the rectangular object.
    gameOverRect.center = (w.screen_x // 2, w.screen_y // 2)


    # Game Over if :
    if s.snake_position[0] < 0 or s.snake_position[0] > w.screen_x - 10:
        w.gameOver(gameOverText, gameOverRect)
    if s.snake_position[1] < 0 or s.snake_position[1] > w.screen_y - 10:
        w.gameOver(gameOverText, gameOverRect)


    for pixel in s.snake_body[1:]:
        if s.snake_position[0] == pixel[0] and s.snake_position[1] == pixel[1]:
            w.gameOver(gameOverText, gameOverRect)


    # Refresh game screen
    pygame.display.update()

    # Frame Per Second
    fps.tick(s.snake_speed)