import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((640, 480))


CHANGE_COLOR_EVENT = pg.USEREVENT + 1

pg.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class ColorBox(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        new_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.image.fill(new_color)

box1 = ColorBox(200, 200)
box2 = ColorBox(400, 200)
group = pg.sprite.Group(box1, box2)

run = True
while run:
    screen.fill((0, 0, 0)) 
    for event in pg.event.get():
        if event.type == pg.QUIT: run = False
        
        
        if event.type == CHANGE_COLOR_EVENT:
            box1.change_color()
            box2.change_color()

    group.draw(screen)
    pg.display.flip()

pg.quit()