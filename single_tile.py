import pygame


class SingleTile(pygame.sprite.Sprite):

    """
        Creates a pygame Sprite representing the scene \n
        :param x: left position in the scene
        :type x: float
        :param y: top position in the scene
        :type y: float
        :param rect: image rect
        :type rect: Union[Rect, RectType]
        :param image: the string value representing the url to the background image of the tile-set
        :type image: str
        :param coordinates: x,y,z representing the indexes in the level array
        :type coordinates: tuple(int, int, int)
        :param value: The numeric value of the tile. Eg: 32 for the Dragon
        :type value: int
    """
    def __init__(self, x, y, rect, image, coordinates, value):

        super().__init__()
        self.image = image
        self.rect = rect
        self.rect.x = x
        self.rect.y = y
        self.coordinates = coordinates
        self.value = value
