import sys
import pygame
import random

width = 400
heigth = 500

pygame.init()

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Hamtaro')
surface_color = (0, 0, 0)
#surface_color = (252, 255, 136, 1)

rect = pygame.Rect(139, 250, 120, 60)
#rect.center = (width // 2, heigth // 2)

#rectangulos que no tendran interaccion
rect_2 = (100, 130, 60, 120)
rect_3 = (237, 130, 60, 120)

print(rect.x)
print(rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(surface_color)

    pygame.draw.rect(surface, (136, 255, 242, 1), rect)
    pygame.draw.rect(surface, (0, 0, 0), rect_2)
    pygame.draw.rect(surface, (0, 0, 0), rect_3)

    pygame.draw.circle(surface, (123, 32, 43), (200, 250), 40)

    pygame.draw.line(surface, (0, 0, 0) ,(0,0), (400,500), 5)
    pygame.draw.line(surface, (0, 0, 0), (0, 500), (400, 0), 5)

    for raw in range(0, 500, 8):
        pygame.draw.polygon(surface, (random.randrange(0, 255, 10), random.randrange(0, 255, 10), random.randrange(0, 255, 10)), ( (random.randrange(0, 500, 10), random.randrange(0, 500, 10)), (random.randrange(0, 500, 10), random.randrange(0, 500, 10)), (random.randrange(0, 500, 10), random.randrange(0, 500, 10),), (random.randrange(0, 500, 10), random.randrange(0, 500, 10)) ))

    pygame.display.update()
