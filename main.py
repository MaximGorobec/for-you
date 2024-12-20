import pygame
import os
import sys
import random
from pygame import Color


def load_image(name, colorkey=Color('white')):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shaders')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("hero.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    clock = pygame.time.Clock()
    point = (1, 1)
    screen.fill((255, 255, 255))

    pygame.mouse.set_visible(True)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (0 <= event.pos[0] <= width) and (0 <= event.pos[1] <= height):
                    point = event.pos
        if random.choice((1, 0)):
            sprite.rect.x += (-1 if (point[0] - sprite.rect.x) < 0 else 1) * 10
        else:
            sprite.rect.y += (-1 if (point[1] - sprite.rect.y) < 0 else 1) * 10
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((255, 255, 255))
        clock.tick(1)
    pygame.display.flip()
