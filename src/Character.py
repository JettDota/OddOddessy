'''
Created on Jan 23, 2015

@author: Alex
'''
import pygame
class Character():
    def __init__(self):
        self.image = pygame.image.load("skin.png")
        self.x=64
        self.ground = 10*32
        self.y=self.ground
        self.clock = pygame.time.Clock()
        self.counter = 0 
        self.vy = 0
        self.gravcount=0
    def draw(self, screen):
        #screen.fill((55,55,55)) #clear screen
        screen.blit(self.image,(self.x,self.y))
        #pygame.display.flip()
    def move(self,dir):
        self.counter+=1
        if(self.counter >1):
            self.counter = 0
            if dir == 0:
                self.x-=8;
            elif dir == 1:
                self.x+=8;
    def jump(self):
        self.vy = -20
    def update(self):
        self.y+= self.vy
    def grav(self):
        if(self.y > self.ground):
            self.y = self.ground
            self.vy=0
            self.gravcount = 1
        elif(self.gravcount==0):
            self.update()
            self.vy+=1
            self.gravcount = 1
        else :self.gravcount-=1