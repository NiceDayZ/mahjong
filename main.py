import pygame
import sys
import mahjong

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game_flag = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


if __name__ == '__main__':
    background = pygame.image.load('Floor.jpg')
    modified_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    tiles = mahjong.Mahjong("ExampleBlack.png")
    single_piece = tiles.create_tile(60, 8, 150, 200, (0, 0), (0, 0, 0), 1)
    single_piece2 = tiles.create_tile(60, 225, 150, 200, (0, 100), (0, 0, 3), 2)
    tile_group = pygame.sprite.Group()
    tile_group.add(single_piece)
    tile_group.add(single_piece2)

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
