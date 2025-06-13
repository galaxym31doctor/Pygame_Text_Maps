import pygame as pg
"""
level = [['x', 'x', 'x', 'x', 'x'],
       ['x', 'o', 'o', 'o', 'x'],
       ['x', 'o', 'o', 'o', 'x'],
       ['x', 'o', 'o', 'o', 'x'],
       ['x', 'o', 'x', 'o', 'x'],
       ['x', 'o', 'o', 'o', 'x'],
       ['x', 'o', 'o', 'o', 'x'],
       ['x', 'x', 'x', 'x', 'x']]
"""
pixel_size = 24
x_between_pixels = 0

with open ('landscape.txt') as file_landscape:
    level = file_landscape.readlines()
       
pg.init()
sc = pg.display.set_mode((640, 480))
pg.display.set_caption('map')
clock = pg.time.Clock()
title_size = 32

def drawMap (sc, level):
    level_high = len(level[0])
    level_width = len(level)
    print (level_high, ' ', level_width)
    w = 0
    h = 0
    for i in range (level_high):
        for j in range (level_width):
            if (level[j][i] == 'x'):
                pg.draw.rect(sc, (255, 255, 255), (h, w, pixel_size, pixel_size))
                w += pixel_size + x_between_pixels                
                pass
            
            elif (level[j][i] == 'o'):
                pg.draw.rect(sc, (100, 100, 100), (h, w, pixel_size, pixel_size))
                w += pixel_size + x_between_pixels
                pass
        h += pixel_size + x_between_pixels
        w = 0
        

def drawGameWindow(sc):
    drawMap(sc, level)
    pg.display.flip()

running = True

drawGameWindow(sc)

while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            
    pg.display.flip()

pg.quit()

