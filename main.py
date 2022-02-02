import random
import sys
import pygame
from pygame.locals import *
import copy

WIDTH = 500 #game window width
HEIGHT = 500 #game window height
FPS = 60 #game's speeds
Pixsize = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window
board = pygame.Surface((WIDTH, HEIGHT))
time_delta = 1/60
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLACK_A = (0,0,0, 255)
WHITE_A = (255, 255, 255, 255)

#BLACK IS 1
#WHITE IS 0

# currently rule 30
BIT_PATTERN = {
    "111": WHITE_A,
    "110": BLACK_A,
    "101": WHITE_A,
    "100": BLACK_A,
    "011": BLACK_A,
    "010": WHITE_A,
    "001": BLACK_A,
    "000": WHITE_A
}

def scan_row(y):
    next_row = []
    for x in range(WIDTH-2):
        case = ""
        for i in range(0, 3):
            if screen.get_at((x+i, y)) == BLACK_A: case+="1"
            else: case+='0'
        bit = copy.deepcopy(case)
        next_row.append(bit)
    return next_row

def place_pixels(y):
    row = scan_row(y)
    for x,cell in enumerate(row):
        screen.set_at((x+1, y+1), BIT_PATTERN.get(cell))

is_running = True
def mainloop():
    flag = False
    pygame.init()
    screen.fill(WHITE)

    #for random starting cells
    # for i in range(WIDTH):
    #     screen.set_at((i, 0), random.randrange(0,1))
    screen.set_at((WIDTH//2, 0), random.randrange(0,1))
    
    while is_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if flag == False:
            for y in range(HEIGHT):
                place_pixels(y)
        
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
        flag = True

mainloop()