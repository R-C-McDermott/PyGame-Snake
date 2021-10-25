# Snake game using the PyGame library for python
#
# By Ryan C. McDermott

import pygame
import time
from random import randrange
pygame.init()
from spritesheet import SpriteSheet

SNAKE_WIDTH = 24
SNAKE_HEIGHT = 24
W_MULT = 32
H_MULT = 24
HEIGHT_BORDER = H_MULT*SNAKE_HEIGHT
WIDTH, HEIGHT = W_MULT*SNAKE_WIDTH, HEIGHT_BORDER + (4 * SNAKE_HEIGHT)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake v1.0")
BACKGROUND = (50, 50, 50)
SNAKE_COLOUR = (0, 255, 0)
FRUIT_COLOUR = (255, 0, 0)
BORDER_COLOUR = (0, 0, 255)
GAME_FONT = pygame.font.SysFont('Times New Roman', 30)
FPS = 15

sprite_sheet = pygame.image.load("assets/Textures.png").convert_alpha()
LOSE_SCREEN = pygame.image.load("assets/LoseScreen.png").convert_alpha()
LOSE_SCREEN = pygame.transform.scale(LOSE_SCREEN, (WIDTH, HEIGHT))

border_line = pygame.Rect(0, HEIGHT_BORDER, WIDTH, SNAKE_HEIGHT // 2)

snake = pygame.Rect((WIDTH // 2) - SNAKE_WIDTH,
                        (HEIGHT_BORDER // 2),
                        SNAKE_WIDTH,
                        SNAKE_HEIGHT)
snake_change_x = 0
snake_change_y = 0

fruit_x = randrange(1, W_MULT) * SNAKE_WIDTH
fruit_y = randrange(1, H_MULT) * SNAKE_HEIGHT
fruit = pygame.Rect(fruit_x, fruit_y, SNAKE_WIDTH, SNAKE_HEIGHT)

def draw_game(snake, fruit, snake_body, score):
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, BORDER_COLOUR, (border_line.x, border_line.y, WIDTH, SNAKE_HEIGHT // 2))
    snake_head = SpriteSheet(sprite_sheet, 384, 384, 2, 0).get_image(8)

    text_surface = GAME_FONT.render(f"Score: {score}", True, BORDER_COLOUR)
    WIN.blit(text_surface, (40, HEIGHT_BORDER + 40))

    if len(snake_body) == 1:
        pygame.draw.rect(WIN, SNAKE_COLOUR, (snake.x, snake.y, SNAKE_WIDTH, SNAKE_HEIGHT))
    else:
        for i in range(len(snake_body)):
            pygame.draw.rect(WIN, SNAKE_COLOUR, (snake_body[i][0], snake_body[i][1], SNAKE_WIDTH, SNAKE_HEIGHT))

    pygame.draw.rect(WIN, FRUIT_COLOUR, (fruit.x, fruit.y, SNAKE_WIDTH, SNAKE_HEIGHT))
    # WIN.blit(snake_head, (snake.x, snake.y))
    pygame.display.update()

def snake_move(snake, key, snake_body):
    global snake_change_x
    global snake_change_y
    if (key[pygame.K_LEFT] and snake.x > 0 and
            (snake.x - SNAKE_WIDTH) not in [snake_list[0] for snake_list in snake_body]):
        snake_change_x = - SNAKE_WIDTH
        snake_change_y = 0
    if (key[pygame.K_RIGHT] and snake.x < WIDTH - SNAKE_WIDTH and
            (snake.x + SNAKE_WIDTH) not in [snake_list[0] for snake_list in snake_body]):
        snake_change_x = SNAKE_WIDTH
        snake_change_y = 0
    if (key[pygame.K_UP] and snake.y > 0 and
            (snake.y - SNAKE_WIDTH) not in [snake_list[1] for snake_list in snake_body]):
        snake_change_y = - SNAKE_HEIGHT
        snake_change_x = 0
    if (key[pygame.K_DOWN] and snake.y < HEIGHT_BORDER - SNAKE_HEIGHT and
            (snake.y + SNAKE_WIDTH) not in [snake_list[1] for snake_list in snake_body]):
        snake_change_y = SNAKE_HEIGHT
        snake_change_x = 0


def main():
    score = 0
    snake_length = 1
    snake_body = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        snake_move(snake, key, snake_body)
        snake.x += snake_change_x
        snake.y += snake_change_y
        snake_body.append([snake.x, snake.y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        if (fruit.x, fruit.y) == (snake.x, snake.y):
            fruit.x = randrange(1, W_MULT) * SNAKE_WIDTH
            fruit.y = randrange(1, H_MULT) * SNAKE_HEIGHT
            snake_length += 1
            score += 1

        draw_game(snake, fruit, snake_body, score)


        if snake.x < 0 or snake.x > (WIDTH - SNAKE_WIDTH):
            run = False
            WIN.blit(LOSE_SCREEN, (0, 0))
            pygame.display.update()
            time.sleep(3)


        if snake.y < 0 or snake.y > (HEIGHT_BORDER - SNAKE_HEIGHT):
            run = False
            WIN.blit(LOSE_SCREEN, (0, 0))
            pygame.display.update()
            time.sleep(3)


    pygame.quit()

if __name__ == '__main__':
    main()