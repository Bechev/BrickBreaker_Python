import pygame
import time
import os
import random
import sys
# import neat-python

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
BRICK_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile_broken.png')),(BRICK_LENGTH, BRICK_WIDTH)), \
                    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_tile.png')),(BRICK_LENGTH, BRICK_WIDTH)), \
                    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'red_tile_broken.png')),(BRICK_LENGTH, BRICK_WIDTH)), \
                    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'red_tile.png')), (BRICK_LENGTH, BRICK_WIDTH))]


LEVEL = [
    [[4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2]],
    [[2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4]],
    [[4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2]],
    [[2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4]],
    [[4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2], [4], [2]]
    ]

def draw_window(win, pad, ball, wall):
    win.blit(BG, (0,0))
    pad.draw(win)
    ball.draw(win)
    for brick in wall:
        if brick.life_points > 0:
            brick.draw(win) 
    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pad = Pad(300,550, PAD_LENGTH, PAD_WIDTH, PAD_IMG)
    ball = Ball(300, 350, BALL_LENGTH, BALL_WIDTH, BALL_IMG)
    wall = []
    for row_index, row in enumerate(LEVEL):
        for column_index, column in enumerate(row):
            brick = Brick((column_index + 1) * BRICK_LENGTH, (row_index + 1) * BRICK_WIDTH, column[0], BRICK_LENGTH, BRICK_WIDTH, BRICK_IMGS)
            wall.append(brick)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        ball.move(pad, wall)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pad.move_left()
        elif keys[pygame.K_RIGHT]:
            pad.move_right()

        draw_window(win, pad, ball, wall)
    
    pygame.quit()
    quit()

main()

