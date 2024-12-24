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
    return image

class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen.get_width() - self.image.get_width())
        self.rect.y = random.randrange(screen.get_height() - self.image.get_height())
        while pygame.sprite.spritecollideany(self, group):
            self.rect.x = random.randrange(screen.get_width() - self.image.get_width())
            self.rect.y = random.randrange(screen.get_height() - self.image.get_height())
        super().__init__(group)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shaders')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    running = True

    all_sprites = pygame.sprite.Group()
    for _ in range(20):
        Bomb(all_sprites)

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    bomb.update(event)
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        clock.tick(20)
    pygame.display.flip()
