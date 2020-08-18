import pygame

class Ball:
    WIN_HEIGHT = 600
    WIN_WIDTH = 800

    def __init__(self, x, y, height, width, img):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = img
        self.vel = 10
        self.xDirection = 1
        self.yDirection = 1
        self.angle = 1

    def move(self, pads, wall, ge, nets):
        # Check if the ball touches the left or right borders of the screen
        if self.x <= 0:
            self.xDirection = 1
        if self.x >= self.WIN_WIDTH - self.width:
            self.xDirection = -1
        
        # Check if the ball touches the top or bottom borders of the screen
        if self.y <= 0:
            self.yDirection = 1

        for index, pad in enumerate(pads):
        
            # If the ball touches the bottom border, trigger a loss
            if self.y >= self.WIN_HEIGHT - self.height:
                # Remove the genome from various lists when loses
                ge[index].fitness -= 1
                pads.pop(index)
                nets.pop(index)
                ge.pop(index)
                self.yDirection= -1 
            
            if self.collide_pad(pad):
                ge[index].fitness += 1
                if self.x >= (pad.x + pad.length/2):
                    self.xDirection = 1
                else:
                    self.xDirection = -1
        
                self.angle = round(abs(((self.x + self.width/2) - (pad.x + pad.length/2))/2) -10)
                self.yDirection *= -1

        if self.collide_wall(wall):
            self.yDirection = -self.yDirection
            ge[index].fitness += 0.1

        self.x += self.xDirection * (self.vel + self.angle)
        self.y +=  self.vel * self.yDirection



    def collide_pad(self, pad):
        pad_mask = pad.get_mask()
        ball_mask = self.get_mask()
        ball_pad_offset = (self.x - pad.x, self.y - round(pad.y))
        
        ball_pad_collision = pad_mask.overlap(ball_mask, ball_pad_offset)

        if ball_pad_collision:
            return True

        return False

    def collide_wall(self, wall):
        ball_mask = self.get_mask()
        for brick in wall:
            if brick.life_points > 0:
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