import pygame
import random

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Part 1")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 40)
        self.rect.y = random.randint(0, SCREEN_HEIGHT // 2)


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
font = pygame.font.SysFont("Arial", 30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        print(f"Score: {score}")

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
