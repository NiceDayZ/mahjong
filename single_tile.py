import pygame


class SingleTile(pygame.sprite.Sprite):

    def __init__(self, x, y, rect, image, coordinates, value):
        super().__init__()
        self.image = image
        self.rect = rect
        self.rect.x = x
        self.rect.y = y
        self.coordinates = coordinates
        self.value = value
