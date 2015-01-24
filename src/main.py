# import the pygame module, so you can use it
import pygame
from Character import Character
# define a main function
def main():
    blocksize = 32
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Odd Oddessy")
    screen = pygame.display.set_mode((1024,612))
    # define a variable to control the main loop
    running = True
    char = Character()
    keys = [0,0]
    # main loop
    while running:
        char.draw(screen)
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
            char.move(0)
        if(keys[0]):
            char.move(1)
        char.grav()
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
