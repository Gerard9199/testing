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