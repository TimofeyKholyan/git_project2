import pygame

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[10] * width for i in range(height)]
        self.left = 130
        self.top = 130
        self.cell_size = 60
        self.x = width
        self.y = height

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            if bool(i) and i % 3 == 0:
                self.top += 1
                pygame.draw.line(screen, (0, 0, 0), (self.left, self.top + i * self.cell_size), (self.left + self.width * self.cell_size, self.top + i * self.cell_size), 3)
            for j in range(self.width):
                if bool(j) and j % 3 == 0:
                    self.left += 1
                    pygame.draw.line(screen, (0, 0, 0), (self.left + j * self.cell_size, self.top), (self.left + j * self.cell_size, self.top + self.height * self.cell_size), 3)
                pygame.draw.rect(screen, {True: (0, 0, 0), False: (255, 0, 0)}[self.board[i][j] >= 0], (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size), {True: 1, False: 3}[self.board[i][j] >= 0])
                if abs(self.board[i][j]) == 1:
                    font = pygame.font.Font(None, 50)
                    number = font.render('1', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 2:
                    font = pygame.font.Font(None, 50)
                    number = font.render('2', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 3:
                    font = pygame.font.Font(None, 50)
                    number = font.render('3', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 4:
                    font = pygame.font.Font(None, 50)
                    number = font.render('4', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 5:
                    font = pygame.font.Font(None, 50)
                    number = font.render('5', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 6:
                    font = pygame.font.Font(None, 50)
                    number = font.render('6', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 7:
                    font = pygame.font.Font(None, 50)
                    number = font.render('7', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 8:
                    font = pygame.font.Font(None, 50)
                    number = font.render('8', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
                if abs(self.board[i][j]) == 9:
                    font = pygame.font.Font(None, 50)
                    number = font.render('9', 1, (100, 100, 255))
                    screen.blit(number, (self.left + j * self.cell_size + (self.cell_size - number.get_width()) // 2, self.top + i * self.cell_size +  + (self.cell_size - number.get_height()) // 2))
            self.left -= 2
        self.top -= 2
        pygame.draw.line(screen, (0, 0, 0), (self.left, self.top), (self.left + self.width * self.cell_size, self.top), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.left, self.top + self.height * self.cell_size), (self.left + self.width * self.cell_size, self.top + self.height * self.cell_size), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.left, self.top), (self.left, self.top + self.height * self.cell_size), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.left + self.width * self.cell_size, self.top), (self.left + self.width * self.cell_size, self.top + self.height * self.cell_size), 3)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i, j = (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        if i >= self.width or j >= self.height or i < 0 or j < 0:
            return None
        else:
            return i, j

    def on_click(self, cell_coords):
        x, y = cell_coords
        if abs(self.x) != self.width and abs(self.y) != self.height:
            self.board[self.y][self.x] *= -1
        self.board[y][x] *= -1
        self.x, self.y = cell_coords


board = Board(9, 9)
clock = pygame.time.Clock()
fps = 60
need = {1, 2, 3, 4, 5, 6, 7, 8, 9}
running = True
screen.fill((255, 255, 255))
while running:
    chosen = abs(board.x) != board.width and abs(board.y) != board.height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and chosen:
            board.board[board.y][board.x] = -1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and chosen:
            board.board[board.y][board.x] = -2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3 and chosen:
            board.board[board.y][board.x] = -3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4 and chosen:
            board.board[board.y][board.x] = -4
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5 and chosen:
            board.board[board.y][board.x] = -5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6 and chosen:
            board.board[board.y][board.x] = -6
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7 and chosen:
            board.board[board.y][board.x] = -7
        if event.type == pygame.KEYDOWN and event.key == pygame.K_8 and chosen:
            board.board[board.y][board.x] = -8
        if event.type == pygame.KEYDOWN and event.key == pygame.K_9 and chosen:
            board.board[board.y][board.x] = -9
    if abs(board.y) != 9 and abs(board.x) != 9:
        board.board[board.y][board.x] *= -1
    for i in range(min(board.width, board.height)):
        if set(board.board[i]) != need:
            break
        if set([j[i] for j in board.board]) != need:
            break
        if set(board.board[i // 3 * 3][i % 3 * 3: i % 3 * 3 + 3] + board.board[i // 3 * 3 + 1][i % 3 * 3: i % 3 * 3 + 3] + board.board[i // 3 * 3 + 2][i % 3 * 3: i % 3 * 3 + 3]) != need:
            break
    else:
        board.board = [[0] * board.width for i in range(board.height)]
    if abs(board.y) != 9 and abs(board.x) != 9:
        board.board[board.y][board.x] *= -1
    screen.fill((255, 255, 255))
    board.render()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()