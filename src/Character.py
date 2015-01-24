'''
Created on Jan 23, 2015

@author: Alex
'''
import pygame
class Character():
    def __init__(self):
        self.image = pygame.image.load("skin.png")
        self.x=64
        self.y=8*32
        self.clock = pygame.time.Clock()
        self.counter = 0 
    def draw(self, screen):
        screen.fill((55,55,55)) #clear screen
        screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    def move(self,dir):
        self.counter+=1
        if(self.counter >12):
            self.counter = 0
            if dir == 0:
                self.x-=8;
            elif dir == 1:
                self.x+=8;
    