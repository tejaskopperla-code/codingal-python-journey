import pygame as pg


pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("My first game screen")  

try:
    raw_img = pg.image.load("subject.png") 
    
    img = pg.transform.scale(raw_img, (300, 300))
except:
    
    img = pg.Surface((300, 300))
    img.fill((200, 0, 0)) 


POS = (100, 100)


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    
    screen.fill((58, 58, 58))

    
    screen.blit(img, POS)

    pg.display.flip()

pg.quit()
