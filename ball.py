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

    def move(self):
        if self.x <= 0 or self.x >= self.WIN_WIDTH -  self.width:
            self.Xvel = -self.Xvel
        if self.y <= 0 or self.y >= self.WIN_HEIGHT - self.height:
            self.Yvel = -self.Yvel
        self.x -= self.Xvel
        self.y -=  self.Yvel

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)