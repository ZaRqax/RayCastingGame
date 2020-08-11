from settings import *
import pygame,math

class  Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

        self.mouse_x = 0
        self.mouse_y = 0
        self.sin_mouse = 0
        self.cos_mouse = 0

    @property
    def pos(self):
        return (self.x,self.y)

    @property
    def mouse_angle(self):
        return {'cos':self.cos_mouse,
                 'sin':self.sin_mouse}

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
        if keys[pygame.K_s]:
            self.y += player_speed
        if keys[pygame.K_d]:
            self.x +=player_speed
        if keys[pygame.K_a]:
            self.x -= player_speed
        if keys[pygame.K_LEFT]:
            self.angle -= .02
        if keys[pygame.K_RIGHT]:
            self.angle  += .02



        if any((self.x > WIDTH,self.x < 0, self.y > HEIGHT, self.y < 0)):
            self.x, self.y = player_pos

        self.mouse_tracking()



    def mouse_tracking(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        a = self.mouse_x - self.x
        b = self.mouse_y - self.y
        c = math.sqrt(a**2 + b**2)
        self.sin_mouse = a / c
        self.cos_mouse = b / c

        #  if self.mouse_pos[0] > self.x and self.mouse_pos[1] < self.y:
        #     self.mouse_pos = (self.mouse_pos[0] ,self.mouse_pos[1]-HEIGHT)
        # elif self.mouse_pos[0] < self.x and self.mouse_pos[1] < self.y:
        #     self.mouse_pos = (self.mouse_pos[0] +WIDTH,self.mouse_pos[1])