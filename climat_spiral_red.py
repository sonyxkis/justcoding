import pygame as pg
import pandas as pd
import math

pg.init()

SIZE = WIDTH, HIGHT  = 800, 800
BG_COLOR = (0,0,0)

clock  = pg.time.Clock()
window = pg.display.set_mode(SIZE)
window.fill(BG_COLOR)

running = True

cycles = [int(WIDTH/2 * i/100) for i in (80,50,20)]
cycle  = math.tau


#data = pd.read_csv('https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv', header=1)
data = pd.read_csv('GLB.Ts+dSST.csv', header=1)


for k in cycles:
    pg.draw.circle(window,(60,80,90),(WIDTH/2,HIGHT/2),k,3)


for t,k in enumerate(cycles, start=-1):
    
    img = pg.font.SysFont(None, 30).render(str(t),True,(255,0,0))
    rect = img.get_rect(center=(WIDTH/2,k))
    pg.draw.rect(window, BG_COLOR, rect)
    window.blit(img,rect)


r = max(cycles)+40
for month in range(1,13):
    teta = cycle / 12 * month 
    pos = r * math.cos(teta- cycle /4) + WIDTH/2, r * math.sin(teta- cycle /4) + HIGHT / 2

    img = pg.font.SysFont(None, 48).render(data.columns[month],True,(255,0,0))
    img = pg.transform.rotate(img, -math.degrees(teta))
    rect = img.get_rect(center=pos)
    window.blit(img,rect)

lines = []

for index, zeile in data.iterrows():
    for i in range(1,13):
        teta = cycle / 12 * i
        if zeile[i] != '***':
            r = (float(zeile[i])-(-1)) / (1- (-1)) * (max(cycles) - min(cycles)) + min(cycles)
            pos = r * math.cos(teta- cycle /4) + WIDTH/2, r * math.sin(teta- cycle /4) + HIGHT / 2

            lines.append((zeile[0], pos , zeile[i]))

pg.display.flip()


clock.tick(1)
for (year,p1,_), (_,p2,anomalie) in zip(lines, lines[1:]):
    pg.draw.line(window, (255,0,0), p1, p2, 3)
    pg.draw.rect(window, BG_COLOR, rect)
    img = pg.font.SysFont(None, 70).render(str(year),True,(255,0,0))
    rect = img.get_rect(center=(WIDTH/2,HIGHT/2))
    window.blit(img,rect)
    
    pg.display.flip()


for k in cycles:
    pg.draw.circle(window,(60,80,90),(WIDTH/2,HIGHT/2),k,3)


for t,k in enumerate(cycles, start=-1):
    
    img = pg.font.SysFont(None, 30).render(str(t),True,(255,255,0))
    rect = img.get_rect(center=(WIDTH/2,k))
    pg.draw.rect(window, BG_COLOR, rect)
    window.blit(img,rect)

pg.display.flip()

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    


    clock.tick(1)
pg.quit()    

    

