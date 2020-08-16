import pygame

class Brick:

    def __init__(self, x, y, life_points, length, width, img):
        self.x = x
        self.y = y
        self.life_points = 1
        self.length = length
        self.width = width
        self.img = img
    
    def hit(self):
        self.life_points -= 1

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)