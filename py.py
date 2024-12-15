import pygame
from pygame import Color
from random import randint
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[randint(1,2) for i in range(height)] for _ in range(width)]
        # значения по умолчанию
        self.left = 20
        self.top = 50
        self.cell_size = 20
        self.t = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, Color('white'), (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                if self.board[x][y] == 1:
                    pygame.draw.circle(screen, Color('red'), (x * self.cell_size + self.left + self.cell_size // 2, y * self.cell_size + self.top + self.cell_size // 2), self.cell_size // 2 - 2)
                elif self.board[x][y] == 2:
                    pygame.draw.circle(screen, Color('blue'), (x * self.cell_size + self.left + self.cell_size // 2, y * self.cell_size + self.top + self.cell_size // 2), self.cell_size // 2 - 2)


    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if 0 <= pos[0] <= self.width - 1 and 0 <=  pos[1] <= self.height - 1:
            return pos
        return None
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)

    def on_click(self, cell):
        if self.board[cell[0]][cell[1]] in (self.t, 0):
            for i in range(self.width):
                self.board[i][cell[1]] = self.t
            for i in range(self.height):
                self.board[cell[0]][i] = self.t
            self.t = 1 if self.t == 2 else 2

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    board = Board(5, 5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.display.flip()