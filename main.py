import pygame
import os
import sys
import random
from pygame import Color


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((1, 1))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shaders')
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    running = True

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("car.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    clock = pygame.time.Clock()
    point = (1, 1)
    screen.fill((255, 255, 255))
    v = 1
    pygame.mouse.set_visible(True)
    sprite.image = pygame.transform.flip(sprite.image, 1, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (0 <= event.pos[0] <= width) and (0 <= event.pos[1] <= height):
                    point = event.pos
        if sprite.rect.collidepoint((0, 0)) :
            sprite.image = pygame.transform.flip(sprite.image, 1, 0)
            v = 1
        elif sprite.rect.collidepoint((width, 0)):
            sprite.image = pygame.transform.flip(sprite.image, 1, 0)
            v = -1
        sprite.rect.x += v
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((255, 255, 255))
        clock.tick(20)
    pygame.display.flip()
