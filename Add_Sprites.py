import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Add Sprites Project")


class Box(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

player = Box((0, 255, 0), 100, 100)
static_box = Box((0, 0, 255), 300, 200) 
all_sprites = pg.sprite.Group(player, static_box)

run = True
while run:
    screen.fill((255, 255, 255)) 
    for event in pg.event.get():
        if event.type == pg.QUIT: run = False

    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:  player.move(-5, 0)
    if keys[pg.K_RIGHT]: player.move(5, 0)
    if keys[pg.K_UP]:    player.move(0, -5)
    if keys[pg.K_DOWN]:  player.move(0, 5)

    all_sprites.draw(screen)
    pg.display.flip()
    pg.time.Clock().tick(60)

pg.quit()