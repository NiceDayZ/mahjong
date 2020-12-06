import pygame
import sys
import mahjong

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

game_flag = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = []


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


if __name__ == '__main__':
    background = pygame.image.load('Assets/Images/Floor.jpg')
    modified_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    import_level('Assets/Levels/level1.txt')

    tiles = mahjong.Mahjong("Assets/Images/ExampleBlack.png")
    # single_piece1 = tiles.create_tile((0, 0, 0), 6)
    # single_piece2 = tiles.create_tile((0, 2, 0), 7)
    # single_piece3 = tiles.create_tile((2, 0, 0), 8)
    tile_group = pygame.sprite.Group()
    # tile_group.add(single_piece1)
    # tile_group.add(single_piece2)
    # tile_group.add(single_piece3)

    for k in range(len(level)):
        for i in range(len(level[k])):
            for j in range(len(level[k][i])):
                if level[k][i][j] != 0:
                    single_piece = tiles.create_tile((j, i, k), level[k][i][j])
                    tile_group.add(single_piece)

    while game_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in tile_group if s.rect.collidepoint(pos)]

        pygame.display.flip()
        screen.blit(modified_background, (0, 0))
        tile_group.draw(screen)
        clock.tick(30)
