import pygame

class Ball:
    WIN_HEIGHT = 600
    WIN_WIDTH = 800

    def __init__(self, x, y, height, width, img):
        self.x = x
        self.y = y
        self.Xvel = 10
        self.Yvel = 10
        self.height = height
        self.width = width
        self.img = img

    def move(self, pad):
        if self.x <= 0 or self.x >= self.WIN_WIDTH -  self.width:
            self.Xvel = -self.Xvel
        
        if self.y <=0:
            self.Yvel = -self.Yvel
        if self.y >= self.WIN_HEIGHT - self.height:
            print("lost")
            self.Yvel = -self.Yvel
        
        if self.collide(pad):
            self.Yvel = -self.Yvel
        self.x -= self.Xvel
        self.y -=  self.Yvel

    def collide(self, pad):
        pad_mask = pad.get_mask()
        ball_mask = self.get_mask()
        ball_offset = (self.x - pad.x, self.y - round(pad.y))

        collision = pad_mask.overlap(ball_mask, ball_offset)
        
        if collision:
            return True
        
        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)