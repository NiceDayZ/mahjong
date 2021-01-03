def get_pixel_values(value):
    return (1 + (((value-1) % 45) * 110)), (1 + ((value-1)//45)*142)


def get_position_values(coordinates):
    return (154+coordinates[0]*35.5) - 112.5 - 7*coordinates[2], 20+coordinates[1]*50 - 100 - 7*coordinates[2]
