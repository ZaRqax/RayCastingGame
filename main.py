import pygame
from settings import *
from player import Player
import math

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.circle(sc,GREEN,player.pos,12)
    # pygame.draw.line(sc,GREEN,player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                        player.y + WIDTH * math.sin(player.angle)),2)
    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * player.mouse_angle['sin'],
                                             player.y + WIDTH * player.mouse_angle['cos']),2)
    pygame.display.flip()
    clock.tick(FPS*4)