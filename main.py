import pygame
from pygame import Color
import pprint
class Board:
    # создание поля
    def __init__(self, width, height):
        self.do_click = True
        self.run = False
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]
        self.left = 20
        self.top = 50
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 1:
                    r = 90
                    c = Color('Green')
                else:
                    r = 1
                    c = Color('White')
                pygame.draw.rect(screen, c, (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), r)
    def get_cell(self, mouse_pos):
        pos = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if pos[0] <= self.width - 1 and pos[1] <= self.height - 1:
            return pos
        return None
    def get_click(self, mouse_pos):
        if self.do_click:
            cell = self.get_cell(mouse_pos)
            if cell != None:
                self.on_click(cell)

    def on_click(self, cell):
        self.board[cell[0]][cell[1]] = abs(self.board[cell[0]][cell[1]] - 1)

    def start(self):
        self.do_click = False
        self.run = True

    def stop(self):
        self.do_click = True
        self.run = False
        print(1)

    def next_move(self):
        past_board = board.board.copy()
        past_board.insert(0, len(past_board[0]) * [0])
        past_board.append(len(past_board[0]) * [0])
        past_board = [[0] + i + [0] for i in past_board]
        for i in range(1, len(past_board) - 1):
            for j in range(1, len(past_board[i]) - 1):
                neighbours = sum((past_board[i - 1][j + 1], past_board[i][j + 1], past_board[i + 1][j + 1],
                                 past_board[i - 1][j]                          , past_board[i + 1][j],
                                 past_board[i - 1][j - 1], past_board[i][j - 1], past_board[i + 1][j - 1]))
                if neighbours == 3:
                    board.board[i - 1][j - 1] = 1
                elif (2 > neighbours) or (neighbours > 3):
                    board.board[i - 1][j - 1] = 0
        past_board = [i[1: - 1]for i in past_board]
        past_board.pop(-1)
        past_board.pop(0)
        if past_board == board.board:
            self.stop()
if __name__ == '__main__':
    fps = 3
    v = 1
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Жизнено')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    board = Board(25, 25)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
                elif event.button == 4:
                    v += 0.1
                elif event.button == 5:
                    v -= 0.1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if board.run == False:
                        board.start()
                    else:
                        board.stop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    board.start()
        if board.run:
            clock.tick(fps * v)
            board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.display.flip()
