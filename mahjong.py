import pygame
import single_tile
import helper


class Mahjong(pygame.sprite.Sprite):
    TILE_HEIGHT = 200
    TILE_WIDTH = 150
    TILE_COLOR_KEY = (205, 232, 255)

    def __init__(self, url):
        super().__init__()
        self.custom_image = pygame.image.load(url).convert()
        self.rect = self.custom_image.get_rect()

    def create_tile(self, coordinates, value):
        x, y = helper.get_pixel_values(value)
        pos_x, pos_y = helper.get_position_values(coordinates)
        self.image = pygame.Surface((self.TILE_WIDTH, self.TILE_HEIGHT))
        self.image.set_colorkey(self.TILE_COLOR_KEY)
        self.image.blit(self.custom_image, (0, 0), pygame.Rect(x, y, self.TILE_WIDTH, self.TILE_HEIGHT))
        self.image = pygame.transform.scale(self.image, (self.TILE_WIDTH//2, self.TILE_HEIGHT//2))
        tile = single_tile.SingleTile(pos_x, pos_y, self.image.get_rect(), self.image, coordinates, value)
        return tile
