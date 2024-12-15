from pygame import Color
from random import randint
import pygame

class Ball():
    def __init__(self, pos, vec):
        self.pos = list(pos)
        self.vec = list(vec)
        self.r = 10

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    li = [screen]
    screen2 = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования выключен
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # сохраняем нарисованное (на втором холсте)
                screen2.blit(screen, (0, 0))
                li.append(screen2.copy())
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                # запоминаем текущие размеры
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    if len(li) > 1:
                        li.pop()
        # рисуем на экране сохранённое на втором холсте
        screen.fill(pygame.Color('black'))
        screen.blit(li[-1], (0, 0))
        if drawing:  # и, если надо, текущий прямоугольник
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
        pygame.display.flip()
    pygame.quit()