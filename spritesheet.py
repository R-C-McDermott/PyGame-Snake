# spritesheet file containing spritesheet class
#
# textures obtained from https://opengameart.org/content/snake-graphics

import pygame

class SpriteSheet:
    def __init__(self, textures, pic_width, pic_height, x_block, y_block):
        self.textures = textures
        self.pic_width = pic_width
        self.pic_height = pic_height
        self.x_block = x_block
        self.y_block = y_block
        self.texture_width = self.x_block * self.pic_width
        self.texture_height = self.y_block * self.pic_height

    def get_image(self, down_scale):
        image = pygame.Surface((self.pic_width, self.pic_height)).convert_alpha()
        image.blit(self.textures, (0, 0), (self.texture_width,
                                           self.texture_height,
                                           self.pic_width,
                                           self.pic_height))
        image = pygame.transform.scale(image, (self.pic_width // down_scale, self.pic_height // down_scale))
        return image

