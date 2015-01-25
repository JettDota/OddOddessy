# import the pygame module, so you can use it
import pygame
from Character import Character
from background import background
from platform import platform
from gameBoard import gameBoard
# define a main function
def main():
    blocksize = 32
    platforms =[platform(0, 18),platform(1, 18),platform(2, 18),]
    def checkForPlatform():
        q=1
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Odd Oddessy")
    screen = pygame.display.set_mode((1024,612))
    # define a variable to control the main loop
    running = True
    char = Character()
    background2 = background()
    gb = gameBoard()
    keys = [0,0]
    # main loop
    def draw ():
        screen.fill((55,55,55))
        background2.draw(screen)
        gb.draw(screen)
        char.draw(screen)
        for i in platforms:
            i.draw(screen,0)
        pygame.display.flip()
    while running:
        draw()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    keys[0]=1
                    char.counter = 0
                if event.key==pygame.K_a:
                    keys[1]=1
                    char.counter = 0
                if event.key==pygame.K_w:
                    char.jump()
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_d:
                    keys[0]=0
                if event.key==pygame.K_a:
                    keys[1]=0
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        if(keys[1]):
            # we nee another check here for the game start
            if char.x <= 250:
                background2.scrollRight()
                gb.moveScreen(0)
            else:
                char.move(0)
            
        if(keys[0]):
            #insert check
            char.move(1)
            if char.x >= 750:
                background2.scrollLeft()
                gb.moveScreen(1)

        char.characterupdate(gb.checkCol)
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
