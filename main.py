# Snake game using the PyGame library for python
#
# By Ryan C. McDermott

import pygame
pygame.init()
from game_objects import Snake
from game_objects import Fruit
from spritesheet import SpriteSheet


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake v1.0")
BACKGROUND = (50, 50, 50)
SNAKE_WIDTH = 48
SNAKE_HEIGHT = 48

FPS = 60

sprite_sheet = pygame.image.load("assets/Textures.png").convert_alpha()

def draw_game(snake):
    snake_head = SpriteSheet(sprite_sheet, 384, 384, 2, 0).get_image(8)
    WIN.blit(snake_head, ((WIDTH // 2) - (SNAKE_WIDTH // 2), (HEIGHT // 2) - (SNAKE_HEIGHT // 2)))
    pygame.display.update()

def main():
    snake = pygame.Rect((WIDTH // 2) - (SNAKE_WIDTH // 2),
                        (HEIGHT // 2) - (SNAKE_HEIGHT // 2),
                        SNAKE_WIDTH,
                        SNAKE_HEIGHT)
    WIN.fill(BACKGROUND)
    pygame.display.update()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_game(snake)
    pygame.quit()

if __name__ == '__main__':
    main()