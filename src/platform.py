'''
Created on Jan 24, 2015

@author: Alex
'''
import pygame
class platform(object):
    '''
    classdocs
    '''

    def __init__(self, x,y):
        '''
        Constructor
        '''
        self.x=x
        self.y=y
        self.size =32
    def draw(self,screen,loc):
        screen.blit(pygame.image.load("Grassland/Grass_Tile1.png"),(self.x*self.size,self.y*self.size))