import pygame
import single_tile
import helper


class Mahjong(pygame.sprite.Sprite):
    """
        Creates a pygame Sprite representing the scene \n
        :param url: the string value representing the url to the background image of the scene
        :type url: str
    """

    TILE_HEIGHT = 140
    TILE_WIDTH = 108
    TILE_COLOR_KEY = (0, 0, 0)

    def __init__(self, url):

        super().__init__()
        self.custom_image = pygame.image.load(url).convert()
        self.rect = self.custom_image.get_rect()

    def create_tile(self, coordinates, value):
        """
        Creates a tile from given information about position in level array and it's value \n
        :param coordinates: x,y,z representing the indexes in the level array
        :type coordinates: tuple(int, int, int)
        :param value: The numeric value of the tile. Eg: 32 for the Dragon
        :type value: int
        :return: a pygame Sprite that represents the created tile
        :rtype: single_tile.SingleTile
        """
        x, y = helper.get_pixel_values(value)
        pos_x, pos_y = helper.get_position_values(coordinates)
        self.image = pygame.Surface((self.TILE_WIDTH, self.TILE_HEIGHT))
        self.image.set_colorkey(self.TILE_COLOR_KEY)
        self.image.blit(self.custom_image, (0, 0), pygame.Rect(x, y, self.TILE_WIDTH, self.TILE_HEIGHT))
        self.image = pygame.transform.scale(self.image, (int(self.TILE_WIDTH/1.4), int(self.TILE_HEIGHT/1.44)))
        tile = single_tile.SingleTile(pos_x, pos_y, self.image.get_rect(), self.image, coordinates, value)
        return tile
