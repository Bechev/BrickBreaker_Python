import pygame
import time
import os
import random
import sys

# Import other classes
sys.path.append("./")
from pad import Pad
from ball import Ball
from brick import Brick



WIN_WIDTH = 800
WIN_HEIGHT = 600

BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.jpg')),(WIN_WIDTH, WIN_HEIGHT))

PAD_LENGTH = 65
PAD_WIDTH = 15
PAD_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pad.png')),(PAD_LENGTH, PAD_WIDTH))

BALL_LENGTH = 15
BALL_WIDTH = 15
BALL_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ball.png')),(BALL_LENGTH, BALL_WIDTH))

BRICK_LENGTH = 50
BRICK_WIDTH = 15
BLUE_BLOCK_IMG = [pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile.png')),(BRICK_LENGTH, BRICK_WIDTH)), \
                  pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile_broken.png')),(BRICK_LENGTH, BRICK_WIDTH))]

RED_BLOCK_IMG = [pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile.png')),(BRICK_LENGTH, BRICK_WIDTH)), \
                 pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile_broken.png')), (BRICK_LENGTH, BRICK_WIDTH))]


def draw_window(win, pad, ball, brick):
    win.blit(BG, (0,0))
    pad.draw(win)
    ball.draw(win)
    brick.draw(win)
    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pad = Pad(300,550, PAD_LENGTH, PAD_WIDTH, PAD_IMG)
    ball = Ball(300, 535, BALL_LENGTH, BALL_WIDTH, BALL_IMG)
    brick = Brick(100, 100, 2, BRICK_LENGTH, BRICK_WIDTH, BLUE_BLOCK_IMG[0])

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        ball.move(pad, brick)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pad.move_left()
        elif keys[pygame.K_RIGHT]:
            pad.move_right()

        draw_window(win, pad, ball, brick)
    
    pygame.quit()
    quit()

main()

