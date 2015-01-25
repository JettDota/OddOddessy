'''
Created on Jan 23, 2015

@author: Alex
'''
import pygame
class Character():
    def __init__(self):
        self.image = pygame.image.load("skin.png")
        self.x=64
        self.y=16*32+1
        self.clock = pygame.time.Clock()
        self.counter = 0 
        self.vy = 0
        self.appex=-100
        self.origin = 0
        
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
        self.vy += -5
        self.origin = self.y
    def update(self, check):
        self.nextY= self.y + self.vy
        if(check(self.x, self.nextY + 64 + self.vy + 5 ) == True):
            self.vy = 0
            self.y = 16*32+1
        else:
            self.y += self.vy
            
    def characterupdate (self, check):
        if(self.y == self.origin + self.appex):
            self.vy = -self.vy
        self.update(check)
        