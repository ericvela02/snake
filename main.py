import pygame
from snake import *
from food import Food

HEIGHT = 600
WIDTH = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
block_size = 20
snake = Snake((WIDTH, HEIGHT), block_size)
clock = pygame.time.Clock()
running = True
food = Food((WIDTH, HEIGHT), block_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.steer(Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                snake.steer(Direction.RIGHT)
            if event.key == pygame.K_UP:
                snake.steer(Direction.UP)
            if event.key == pygame.K_DOWN:
                snake.steer(Direction.DOWN)

    
    snake.move()
    screen.fill("white")
    snake.draw(pygame, screen)
    food.draw(pygame, screen)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()