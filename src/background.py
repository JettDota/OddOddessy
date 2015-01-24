'''
Created on Jan 23, 2015

@author: Carl W Glahn
'''
import pygame
import sys
import pygame.sprite
class background():
    def __init__(self):
        self.positions = [3]
        self.dasClock = pygame.time.Clock()
        self.image1 = pygame.image.load("Bohinj_1000x600.jpg")
        self.image2 = pygame.image.load("P1010376.jpg")
        self.image2 = pygame.image.load("wallpaper_1000x600_swirl.jpg")
   
    #background_size = background.get_size()
    #background_rect = background.get_rect()
    #screen = pygame.display.set_mode(background_size)
    
    
    
    #width, height = background_size
    
    # x=0
    #y=0

    def scrollLeft(self):
        self.i = 0
        self.screenZero = -1;
        for self.i in range (3):
            self.positions[self.i] -= 5
            if (self.positions[self.i] == 0):
                self.screenZero = self.i
        if(self.screenZero != -1):
            if(self.screenZero == 0):
                self.positions[2] = self.positions[1]+1000
            if(self.screenZero == 1):
                self.positions[0] = self.positions[2]+1000
            if(self.screenZero == 2):
                self.positions[1] = self.positions[0]+1000
            #everytime your moving right and a frame is at 0, flip it to the
    def draw(self, screen):
        
        screen.blit(self.image1, (self.positions[0], 0))
        screen.blit(self.image2, (self.positions[1], 0))
        screen.blit(self.image3, (self.positions[2], 0))
        