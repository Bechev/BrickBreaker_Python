import pygame
import time
import os
import random
import sys



# Import other classes
sys.path.append("./")
from pad import Pad


WIN_WIDTH = 800
WIN_HEIGHT = 600

PAD_LENGTH = 65
PAD_WIDTH = 15
PAD_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pad.png')),(PAD_LENGTH, PAD_WIDTH))
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.jpg')),(WIN_WIDTH, WIN_HEIGHT))
BLUE_BLOCK_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'blue_tile.png'))), \
                  pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'blue_tile_broken.png')))]
RED_BLOCK_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'blue_tile.png'))), \
                 pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'blue_tile_broken.png')))]


def draw_window(win, pad):
    win.blit(BG, (0,0))
    pad.draw(win)
    pygame.display.update()

def main():
    pad = Pad(200,550, PAD_LENGTH, PAD_WIDTH, PAD_IMG)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pad.move_left()
        elif keys[pygame.K_RIGHT]:
            pad.move_right()

        draw_window(win, pad)
    
    pygame.quit()
    quit()

main()

