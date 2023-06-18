import pygame as pg
#import pandas as pd
#import math



pg.init()

WIDTH = 800
HIGHT = WIDTH
BG_COLOR = "black"
clock = pg.time.Clock()
window = pg.display.set_mode((WIDTH,HIGHT))
running = True

kreise = [WIDTH/2 * i/100 for i in (20,50,80)]

#print(kreise)



while running:
    window.fill(BG_COLOR)

    for k in kreise:
        pg.draw.circle(window,(60,80,90),(WIDTH/2,HIGHT/2),k,3)
    
    


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    

    pg.display.flip()

    clock.tick(30)
pg.quit()    

    

