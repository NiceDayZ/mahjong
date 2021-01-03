import pygame
import sys
import mahjong

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

game_flag = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = []
selected = None


def check_if_selectable(tile):
    x, y, z = tile.coordinates[0], tile.coordinates[1], tile.coordinates[2]
    if z == (len(level) - 1):
        if (level[z][y][x + 2] == 0 and
                level[z][y + 1][x + 2] == 0 and
                level[z][y - 1][x + 2] == 0) or \
            (level[z][y][x - 2] == 0 and
                level[z][y + 1][x - 2] == 0 and
                level[z][y - 1][x - 2] == 0):
            return True
    else:
        if (level[z + 1][y][x] == 0 and
                level[z + 1][y][x + 1] == 0 and
                level[z + 1][y][x - 1] == 0 and
                level[z + 1][y + 1][x] == 0 and
                level[z + 1][y + 1][x + 1] == 0 and
                level[z + 1][y + 1][x - 1] == 0 and
                level[z + 1][y - 1][x] == 0 and
                level[z + 1][y - 1][x + 1] == 0 and
                level[z + 1][y - 1][x - 1] == 0):
            if (level[z][y][x + 2] == 0 and
                level[z][y + 1][x + 2] == 0 and
                level[z][y - 1][x + 2] == 0) or \
                    (level[z][y][x - 2] == 0 and
                     level[z][y + 1][x - 2] == 0 and
                     level[z][y - 1][x - 2] == 0):
                return True

    return False


def import_level(file):
    global level
    with open(file) as f:
        h, m = [int(x) for x in next(f).split()]
        for index in range(h):
            plane = []
            counter = 0
            for line in f:  # read rest of lines
                counter += 1
                plane.append([int(x) for x in line.split()])
                if counter == m:
                    break
            level.append(plane)


def check_if_win():
    for z in range(len(level)):
        for x in range(len(level[z])):
            for y in range(len(level[z][x])):
                if level[z][x][y] != 0:
                    return False
    return True


def refresh_scene():
    tile_grp = pygame.sprite.Group()

    for z in range(len(level)):
        for y in range(len(level[z][0])):
            for x in range(len(level[z])):
                if level[z][x][y] != 0:
                    single_tile_piece = tiles.create_tile((y, x, z), level[z][x][y])
                    tile_grp.add(single_tile_piece)

    return tile_grp


def deselect_tile():
    global selected
    selected = None
    for z in range(len(level)):
        for x in range(len(level[z])):
            for y in range(len(level[z][x])):
                if level[z][x][y] > 36:
                    level[z][x][y] = level[z][x][y] - 36


if __name__ == '__main__':
    background = pygame.image.load('Assets/Images/Floor.jpg')
    modified_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    import_level('Assets/Levels/level1.txt')

    tiles = mahjong.Mahjong("Assets/Images/Example_3D_2.png")
    tile_group = refresh_scene()

    while game_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in tile_group if s.rect.collidepoint(pos)]
                if len(clicked_sprites) > 0:
                    clicked_tile = clicked_sprites[0]
                    for clicked_sprite in clicked_sprites:
                        if clicked_sprite.coordinates[2] > clicked_tile.coordinates[2]:
                            clicked_tile = clicked_sprite
                    if check_if_selectable(clicked_tile):
                        if selected is None:
                            selected = clicked_tile
                            coord = clicked_tile.coordinates
                            level[coord[2]][coord[1]][coord[0]] = level[coord[2]][coord[1]][coord[0]] + 36
                            # TODO: Differentiate between selected and normal
                        else:
                            if selected.value == clicked_tile.value:
                                coordinates_1 = clicked_tile.coordinates
                                coordinates_2 = selected.coordinates
                                level[coordinates_1[2]][coordinates_1[1]][coordinates_1[0]] = 0
                                level[coordinates_2[2]][coordinates_2[1]][coordinates_2[0]] = 0

                                if check_if_win():
                                    sys.exit(0)
                            deselect_tile()
                else:
                    deselect_tile()

        tile_group = refresh_scene()
        pygame.display.flip()
        screen.blit(modified_background, (0, 0))
        tile_group.draw(screen)
        clock.tick(30)
