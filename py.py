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
    ball_pos = [width // 2, height // 2]
    ball_n_pos = ball_pos
    v = 10
    fps = 60
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                ball_n_pos = event.pos
        if ball_n_pos[1] != ball_pos[1]:
            ball_pos[1] += (ball_n_pos[1] - ball_pos[1]) / abs(ball_n_pos[1] - ball_pos[1])
        if ball_n_pos[0] != ball_pos[0]:
            ball_pos[0] += (ball_n_pos[0] - ball_pos[0]) / abs(ball_n_pos[0] - ball_pos[0])

        pygame.draw.circle(screen, Color('red'), ball_pos, 20)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        clock.tick(fps)
    pygame.quit()