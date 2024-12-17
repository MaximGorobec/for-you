import pygame
from pygame import Color
from random import choice


class Board:
    def __init__(self, width, height):
        self.do_click = True
        self.run = False
        self.width = width
        self.height = height
        self.board = [[choice((10, -1, -1, -1)) for i in range(height)] for _ in range(width)]
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
                r = 1
                c = Color('White')
                if self.board[x][y] == 10:
                    r = 90
                    c = Color('Red')
                elif self.board[x][y] != -1:
                    text = font.render(str(self.board[x][y]), True, Color(0, 255, 0))
                    place = text.get_rect(center=(x * self.cell_size + self.left + 15, y * self.cell_size + self.top + 15))
                    text.get_rect()
                    screen.blit(text, place)
                pygame.draw.rect(screen, c, (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), r)

    def open_cell(self, cell):
        if self.board[cell[0]][cell[1]] == -1:
            r1 = 0
            if cell[1] < self.height - 1:
                if (cell[0] > 0):
                    r1 += abs(self.board[cell[0] - 1][cell[1] + 1]) // 10
                r1 += abs(self.board[cell[0]][cell[1] + 1]) // 10
                if (cell[0] < self.width - 1):
                    r1 += abs(self.board[cell[0] + 1][cell[1] + 1]) // 10

            r2 = 0
            if (cell[0] < self.width):
                if (cell[0] > 0):
                    r2 += abs(self.board[cell[0] - 1][cell[1]]) // 10
                if (cell[0] < self.width - 1):
                    r2 += abs(self.board[cell[0] + 1][cell[1]]) // 10

            r3 = 0
            if cell[1] > 0:
                if (cell[0] > 0):
                    r3 += abs(self.board[cell[0] - 1][cell[1] - 1]) // 10
                r3 += abs(self.board[cell[0]][cell[1] - 1]) // 10
                if (cell[0] < self.width - 1):
                    r3 += abs(self.board[cell[0] + 1][cell[1] - 1]) // 10

            self.board[cell[0]][cell[1]] = sum((r1, r2, r3))

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
        self.open_cell(cell)

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
    pygame.init()
    font = pygame.font.Font(None, 15)
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
