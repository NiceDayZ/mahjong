def get_pixel_values(value):
    """
    Calculates the coordinates of the top-left corner of a tile from the asset image according to it's value \n
    :param value: The numeric value of the tile. Eg: 32 for the Dragon
    :type value: int
    :return: x,y representing the coordinates of the top-left corner in the image
    :rtype: tuple(float, float)
    """
    return (1 + (((value-1) % 36) * 110)), (1 + ((value-1)//36)*142)


def get_position_values(coordinates):
    """
    Calculates the position on screen of a tile according to it's coordinates in the level array \n
    :param coordinates: x,y,z representing the indexes in the level array
    :type coordinates: tuple(int, int, int)
    :return: x,y representing the coordinates of the top-left where the tile should be positioned in the scene
    :rtype: tuple(float, float)
    """
    return (154+coordinates[0]*35.5) - 112.5 - 7*coordinates[2], 20+coordinates[1]*50 - 100 - 7*coordinates[2]
