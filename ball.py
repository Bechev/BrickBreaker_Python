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

    def move(self, pad, wall):
        if self.x <= 0 or self.x >= self.WIN_WIDTH - self.width:
            self.Xvel = -self.Xvel
        
        if self.y <= 0:
            self.Yvel = -self.Yvel
        if self.y >= self.WIN_HEIGHT - self.height:
            print("lost")
            self.Yvel = -self.Yvel
        
        if self.collide(pad, wall):
            self.Yvel = -self.Yvel
        self.x -= self.Xvel 
        self.y -=  self.Yvel

    def collide(self, pad, wall):
        pad_mask = pad.get_mask()
        ball_mask = self.get_mask()
        ball_pad_offset = (self.x - pad.x, self.y - round(pad.y))
        
        ball_pad_collision = pad_mask.overlap(ball_mask, ball_pad_offset)

        if ball_pad_collision:
            return True

        for brick in wall:
            brick_mask = brick.get_mask()
            ball_brick_offset = (self.x - brick.x, self.y - round(brick.y))
            
            ball_brick_collision = brick_mask.overlap(ball_mask, ball_brick_offset)
            
            if ball_brick_collision:
                brick.hit()
                return True


        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)