import pygame

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 130
        self.top = 130
        self.cell_size = 60

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
                pygame.draw.rect(screen, (0, 0, 0), (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size), 1)
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
        if i >= self.width or j >= self.height or i < 0 or i < 0:
            return None
        else:
            return i, j

    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[y][x] = 1

board = Board(9, 9)
clock = pygame.time.Clock()
fps = 5
running = True
chosen = False
screen.fill((255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if event.type == pygame.K_1 and chosen:
            pass
    screen.fill((255, 255, 255))
    board.render()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()