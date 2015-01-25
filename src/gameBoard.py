'''
Created on Jan 24, 2015

@author: Alex
'''
import pygame
from platform import platform
from pygame.examples.headless_no_windows_needed import screen
class gameBoard(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.size = 256
        self.pixelsize = 256*32
        self.pixelloc = 0
        self.platforms = [None]*20[None]*256
        for i in range(0,256):
            self.platforms[19][i]=platform(i,19)
    def draw(self,screen):
        for i in self.platforms:
            i.draw(screen,self.pixelloc)
            
    def moveScreen(self,right):
        if(right):
            self.pixelloc-=8
        elif(right==False):
            self.pixelloc+=8
    def checkCol(self,x,y):
        for i in range(0,20):
            for j in range(0,256):
                if(self.platforms[i][j]!=None):
                    if(i*32<y and i*32+32>y):
                        if(j*32<x and j*32+32>x):
                            return True
        return False