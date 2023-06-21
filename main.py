import pygame
from snake import *
from food import Food

HEIGHT = 800
WIDTH = 800

BLOCK_SIZE = 40

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

snake = Snake((WIDTH, HEIGHT), BLOCK_SIZE)
food = Food((WIDTH, HEIGHT), BLOCK_SIZE)

clock = pygame.time.Clock()
running = True

logo = pygame.image.load('./assets/images/snake-logo.png')
logo_rect = logo.get_rect()
logo_width, logo_height = logo_rect.width, logo_rect.height
background = pygame.image.load('./assets/images/snake-bg.png')

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
    
    window.blit(background, (0, 0))
    
    snake.move()
    snake.check_for_food(food)
    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        snake.respawn()
        food.respawn()
    snake.draw(pygame, window)
    food.draw(pygame, window)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()