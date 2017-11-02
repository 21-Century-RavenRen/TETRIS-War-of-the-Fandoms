'''
@author:21_Century_RavenRen 
'''

import pygame, sys, os, math
from pygame.locals import *
from random import randint

class Game:
    #####Variable#####
    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 768
    GAMENAME = "TETRIS: War of the Fandoms"
    FRAMERATE = 60
    BGCOLOR = (255,255,255)
    playing = False
    
    #####Constructor#####
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption(self.GAMENAME)
        
    def main(self):
        #####Game Loop#####
        while self.playing:
            delta=clock.tick(self.FRAMERATE)
            
            #####Event Handeling#####
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
   
    def quit(self):
        pygame.quit()
        sys.exit()
    
if __name__=="__main__":
        game = Game()
        game.main()