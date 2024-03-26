import pygame
from snake import *
from food import Food


class States(Enum):
    MENU = 1
    GAME = 2
    GAME_OVER = 3


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

logo = pygame.image.load("./assets/images/snake-logo.png")
logo_rect = logo.get_rect()
logo_width, logo_height = logo_rect.width, logo_rect.height
background = pygame.image.load("./assets/images/snake-bg.png")

state = States.MENU

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
            if event.key == pygame.K_SPACE:
                if state == States.GAME_OVER:
                    state = States.GAME
                    snake.respawn()
                    food.respawn()
                elif state == States.MENU:
                    state = States.GAME

    window.blit(background, (0, 0))

    # Game state machine
    if state == States.MENU:

        window.blit(
            logo,
            ((WIDTH // 2 - logo_width // 2), (HEIGHT // 2 - logo_height // 2) - 150),
        )

    elif state == States.GAME:

        snake.move()
        snake.check_for_food(food)
        if snake.check_bounds() == True or snake.check_tail_collision() == True:
            state = States.GAME_OVER
            continue
        snake.draw(pygame, window)
        food.draw(pygame, window)

    elif state == States.GAME_OVER:

        game_over = pygame.font.Font(None, 74).render("Game Over", True, "black")
        game_over_rect = game_over.get_rect()
        game_over_width, game_over_height = game_over_rect.width, game_over_rect.height
        window.blit(
            game_over,
            (WIDTH // 2 - game_over_width // 2, HEIGHT // 2 - game_over_height // 2),
        )

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
