# -*-coding:UTF-8-*-
import sys
import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")
myfont = pygame.font.Font(None, 60)


color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x - radius, y - radius, radius * 2, radius * 2
piece1 = False
piece2 = False
piece3 = False
piece4 = False

start_angle1 = math.radians(0)
end_angle1 = math.radians(90)
start_angle2 = math.radians(90)
end_angle2 = math.radians(180)
start_angle3 = math.radians(180)
end_angle3 = math.radians(270)
start_angle4 = math.radians(270)
end_angle4 = math.radians(360)


screen.fill((0, 0, 255))
# draw the numbers
textImg1 = myfont.render("1", True, color)
screen.blit(textImg1, (x + radius/2 - 20, y - radius/2))
textImg2 = myfont.render("2", True, color)
screen.blit(textImg2, (x - radius/2, y - radius/2))
textImg3 = myfont.render("3", True, color)
screen.blit(textImg3, (x - radius/2, y + radius/2))
textImg4 = myfont.render("4", True, color)
screen.blit(textImg4, (x + radius/2, y + radius/2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True
    # should the pieces be drawn
    if piece1:
        pygame.draw.arc(screen, color, position, start_angle1, end_angle1, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
    if piece2:
        pygame.draw.arc(screen, color, position, start_angle2, end_angle2, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if piece3:
        pygame.draw.arc(screen, color, position, start_angle3, end_angle3, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
    if piece4:
        pygame.draw.arc(screen, color, position, start_angle4, end_angle4, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)

    # is the pie finished
    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0
    pygame.display.update()
