'''
Created on Jan 24, 2015

@author: Alex
'''
import pygame
from platform import platform
class gameBoard(object):
    def __init__(self):
        self.size = 256
        self.pixelsize = 256*32
        self.pixelloc = 0
        self.platforms = [[-1 for x in range (256)]for y in range (0,20)]
        for i in range(0,256):
            self.platforms[19][i]=platform(i,18)
        self.platforms[10][100]
    def draw(self,screen):
        for i in range(20):
            for j in range((int)(self.pixelloc/32),(int)(self.pixelloc/32)+33):
                if(self.platforms[i][j]!=-1):
                    self.platforms[i][j].draw(screen,self.pixelloc)
            
    def moveScreen(self,right):
        if(right):
            self.pixelloc-=1
        elif(right==False):
            self.pixelloc+=8
    def checkCol(self,x,y):
        for i in range(0,20):
            for j in range(0,256):
                if(self.platforms[i][j]!=-1):
                    if(i*32<=y and i*32+32>=y):
                        if(j*32<=x and j*32+32>=x):
                            return True
        return False