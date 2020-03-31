import pygame
from functions import *

#Initialize Screen
pygame.init()
screen_size = screen_width, screen_height = 500, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Haptic Simulation")

#Initialize Electrodes
elec_pos = pos_x, pos_y = int(screen_width / 3), int(screen_height / 4)
elec_rad = rad = 25

#Colors
black = 0, 0, 0
white = 255, 255, 255
gray = 75, 75, 75

#Framerate
fps = 60
frame = 0
delay = 350

#Characters
chars = {'null': [[0,0]], 'capital': [[1,3]], 'a': [[2,1]], 'b': [[2,1] , [2,2]], 'c': [[2,1] , [1,1]], 'd': [[2,1] , [1,1] , [1,2]], 'e': [[2,1] , [1,2]], 'f': [[2,1] , [2,2] , [1,1]], 'g':  [[2,1] , [2,2] , [1,1] , [1,2]], 'h': [[2,1] , [2,2] , [1,2]], 'i': [[2,2] , [1,1]], 'j': [[2,2] , [1,1] , [1,2]], 'k': [[2,1] , [2,3]], 'l': [[2,1] , [2,2] , [2,3]], 'm': [[2,1] , [2,3] , [1,1]], 'n': [[2,1] , [2,3] , [1,1] , [1,2]], 'o': [[2,1] , [2,3] , [1,2]], 'p': [[2,1] , [2,2] , [2,3] , [1,1]], 'q': [[2,1] , [2,2] , [2,3] , [1,2]], 'r': [[2,1] , [2,2] , [2,3] , [1,2]], 's': [[2,2] , [2,3] , [1,1]], 't': [[2,2] , [2,3] , [1,1] , [1,2]], 'u': [[2,1] , [2,3] , [1,3]], 'v': [[2,1] , [2,2] , [2,3] , [1,3]], 'w': [[2,2] , [1,1] , [1,2] , [1,3]], 'x': [[2,1] , [2,3] , [1,1] , [1,3]], 'y': [[2,1] , [2,3] , [1,1] , [1,2] , [1,3]], 'z': [[2,1] , [2,3] , [1,2] , [1,3]], ',': [[2,2]], ';': [[2,2] , [2,3]], ':': [[2,2] , [1,2]], '._period': [[2,2] , [1,2] , [1,3]], '._decimal': [[1,1]  , [1,3]], '!': [[2,2] , [2,3] , [1,2]], '?': [[2,2] , [2,3] , [1,3]], ' ': [[100,100]], '-': [[2,3] , [1,3]], '"_open': [[2,2] , [2,3] , [1,3]], '"_closed': [[2,3] , [1,2] , [1,3]], '#': [[2,3], [1,1] , [1,2] , [1,3]], 'number': [[2,3] , [1,1] , [1,2] , [1,3]], '0': [[2,2] , [1,1] , [1,2]], '1': [[2,1]], '2': [[1,1] , [2,2]], '3': [[2,1] , [1,1]], '4': [[2,1] , [1,1] , [1,2]], '5': [[2,1] , [1,2]], '6': [[2,1] , [2,2] , [1,1]], '7': [[2,1] , [2,2] , [1,1] , [1,2]], '8': [[2,1] , [2,2] , [1,2]], '9': [[2,2] , [1,1]]}

def main(run = True):

    while run:
        #Set Framerate
        clock = pygame.time.Clock()
        clock.tick(fps)
      
        #Check for Exit
        check_quit()

        #Get Input
        phrase = get_input()
        
        #Activate Electrodes      
        count = 0  
        index = 0
        for i in phrase:

            #Check Open or Closed Quotes
            if i == '"':
                if count == 0:
                    activate(chars['"_open'])
                    count = 1
                else:
                    activate(chars['"_closed'])
                    count = 0

            #Check for Decimal or Period
            if i == '.':
                if phrase[index + 1] == ' ':
                    activate(chars['._period'])
                else:
                    activate(chars['._decimal'])

            #Check for Number
            if i in '0123456789':
                activate(chars['number'])
                activate(chars[i])

            #Check for Capaital
            if i.isupper():
                activate(chars['capital'])
                activate(chars[i.lower()])

            else:
                activate(chars[i])

            index += 1


def setup():
    deactivate()
    main()

if __name__ == '__main__':
    setup()

