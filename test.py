import sys
import pygame

class Rectt:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.surface = pygame.display.set_mode((self.width, self.heigth))

    def surface_color(self, R, G, B):
        surface_color = (R, G, B)
        self.surface.fill(surface_color)

    def window_tittle(self, text):
        pygame.display.set_caption(text)

    def rect_color(self, R, G, B):
        self.rect_color = (R, G, B)

    def draw_rect(self, x, y, width, heigth):
        self.rect = (x, y, width, heigth)
        pygame.draw.rect(self.surface, self.rect_color, self.rect)

    def center_rect(self):
        self.rect.center = (self.width // 2, self.heigth // 2)
        self.rect.center

class Test:
    x = 0
    y = 0

    def __init__(self, x):
        self.x = x
        self.y = y

    def recta(self):
        return (test.y - self.y)/(test.x - self.x)

class Beta:

    def __inti__(self, stock_first_price, stock_last_price, composite_first_price, composite_last_price):
        self.stock_first_price = stock_first_price
        self.stock_last_price = stock_last_price
        self.composite_first_price = composite_first_price
        self.composite_last_price = composite_last_price

    def stock_rend(self):
        stock_rend = (self.stock_last_price - self.stock_first_price) / self.stock_last_price
        return stock_rend

    def composite_rend(self):
        composite_rend = (self.composite_last_price - self.composite_first_price) / self.composite_last_price
        return composite_rend

    def stock_beta(self):
        stock_beta = (self.composite_last_price - self.stock_last_price) / (self.composite_first_price - self.stock_first_price)
        return stock_beta

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Rectt = Rectt(400, 500)

    Rectt.surface_color(0, 0, 0)
    Rectt.window_tittle('Hamtaro')
    Rectt.rect_color(15, 100, 50)
    Rectt.draw_rect(120, 100, 120, 60)
    #Rectt.center_rect()

    pygame.display.update()
