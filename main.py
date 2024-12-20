import pygame
import os
import sys
import random


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
    sprite.image = load_image("arrow.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    pygame.mouse.set_visible(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    if (0 <= event.pos[0] <= width) and (0 <= event.pos[1] <= height):
                        sprite.rect.x = event.pos[0]
                        sprite.rect.y = event.pos[1]
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.display.flip()
