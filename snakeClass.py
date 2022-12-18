import pygame

class Snake:
    def __init__(self):
        # snake position at the start
        self.snake_position = [50, 10]
        self.snake_speed = 10
        self.direction = 'right'
        self.change_to = self.direction

        # blocks of the snake body
        self.snake_body = [[50, 10],
                      [40, 10],
                      [30, 10],
                      [20, 10]
                      ]

    def chooseSpeed(self):
        self.speedchoice = int(input("Choose snake speed : normal (1), fast (2), very fast (3): "))

        if (self.speedchoice == 1):
            self.snake_speed = 15


        elif (self.speedchoice == 2):
            self.snake_speed = 30


        elif (self.speedchoice == 3):
            self.snake_speed = 40


        else:
            print("Wrong choice ! ")
            self.chooseSpeed()

    def snakeMovement(self):
        # Key movements
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'up'
                if event.key == pygame.K_DOWN:
                    self.change_to = 'down'
                if event.key == pygame.K_LEFT:
                    self.change_to = 'left'
                if event.key == pygame.K_RIGHT:
                    self.change_to = 'right'


        # Movements conditions
        if self.change_to == 'up' and self.direction != 'down':
            self.direction = 'up'
        if self.change_to == 'down' and self.direction != 'up':
            self.direction = 'down'
        if self.change_to == 'left' and self.direction != 'right':
            self.direction = 'left'
        if self.change_to == 'right' and self.direction != 'left':
            self.direction = 'right'

        # Moving the snake
        if self.direction == 'up':
            self.snake_position[1] -= 10
        if self.direction == 'down':
            self.snake_position[1] += 10
        if self.direction == 'left':
            self.snake_position[0] -= 10
        if self.direction == 'right':
            self.snake_position[0] += 10