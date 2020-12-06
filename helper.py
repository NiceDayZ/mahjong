def get_pixel_values(value):
    return (60 + (((value-1) % 10) * 272)), (8 + ((value-1)//10)*217)


def get_position_values(coordinates):
    return (114+coordinates[0]*37.5), 20+coordinates[1]*50
