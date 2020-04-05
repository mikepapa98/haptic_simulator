import pygame
from haptic_sim import *


def activate(char):
    screen.fill(black)
    for y in range(-1,2):
        deactivate()
        for x in range(len(char)):
            if (pos_x * char[x][0] + pos_x * y >= pos_x and pos_x * char[x][0] + pos_x * y <= screen_width - pos_x):
                pygame.draw.circle(screen,white,(pos_x * 3 - pos_x * char[x][0] - pos_x * y, pos_y * char[x][1]), rad)
                pygame.display.flip()
        pygame.time.delay(delay)
    deactivate()

def deactivate():
    for x in range(1,3):
        for y in range(1,4):
            pygame.draw.circle(screen,gray,(pos_x * x, pos_y * y), rad)
            pygame.display.flip()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def get_input():
    phrase = input("Enter a phrase: ")
    return phrase