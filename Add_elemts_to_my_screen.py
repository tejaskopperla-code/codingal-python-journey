import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("my first game")


RECT_POS = (220, 190, 200, 100)
COLOR_RECT = (0, 255, 0) 


font = pg.font.SysFont("Arial", 40)
text = font.render("My first game ", True, (255, 255, 255))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: run = False
    
    
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, COLOR_RECT, RECT_POS)
    screen.blit(text, (180, 100))
    
    pg.display.flip()

pg.quit()
