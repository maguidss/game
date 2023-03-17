import pygame

ROWS = 5
COLUMNS = 4
BLOCK_SIZE = 80


class GameBoard:
     def __init__(self, ROWS, COLUMNS, BLOCK_SIZE):
          self.rows = ROWS
          self.cols = COLUMNS
          self.BLOCK_SIZE = BLOCK_SIZE
          self.board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

     def draw_board(self, surface):
        surface.fill('Pink')
        for i in range(self.rows):
            for j in range (self.cols):
                x = j * self.BLOCK_SIZE
                y = i * self.BLOCK_SIZE
                pygame.draw.rect(surface, 'Red', (x, y, self.BLOCK_SIZE, self.BLOCK_SIZE), 1)
                if self.board[i][j] != 0:
                        pygame.draw.rect(surface, 'Black', (x+1, y+1, self.BLOCK_SIZE-2, self.BLOCK_SIZE-2))

