import pygame
import single_tile


class Mahjong(pygame.sprite.Sprite):
    def __init__(self, url):
        super().__init__()
        self.custom_image = pygame.image.load(url).convert()
        self.rect = self.custom_image.get_rect()

    def create_tile(self, x, y, width, height, pos, coordinates, value):
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((205, 232, 255))
        self.image.blit(self.custom_image, (0, 0), pygame.Rect(x, y, width, height))
        self.image = pygame.transform.scale(self.image, (width//2, height//2))
        tile = single_tile.SingleTile(pos[0], pos[1], self.image.get_rect(), self.image, coordinates, value)
        return tile
