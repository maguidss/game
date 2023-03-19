import pygame
import sys
import random

#ecrã
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('PuzzlePacked IQ Games')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
background_surf = pygame.image.load('_resources\images\_background.jpg').convert()

#level button
level_background_surf = pygame.Surface((500,60))
level_background_surf.fill('Blue')
level_surf = test_font.render('Level', False, 'White')
level_rect = level_surf.get_rect(center = (250, 30))
pygame.draw.rect(screen, 'Red', level_rect, 4)

#game board
board = pygame.surface.Surface((320, 400))
board.fill('Pink')

#board
#-------------------------------------------------------------------
rectangles_center = {}
class Board:
    def draw_board(surface, rows, columns, block_size, rectangles_center):
        #surface.fill('Pink')
        for i in range(rows):
            for j in range(columns):
                x = j * block_size
                y = i * block_size
                surf_rect = pygame.surface.Surface((block_size, block_size))
                rect = surf_rect.get_rect(topleft = (x,y))
                pygame.draw.rect(surface, 'Pink', (x, y, block_size, block_size), 0)
                #guide lines
                #pygame.draw.rect(surface, 'Red', (x, y, block_size, block_size), 1)
                
                #center of the rectangles position
                key = 'rect' + str(i+1) + str(j+1)
                rectangles_center[key] = rect.center

    def draw_border(surface):    
        border = pygame.draw.polygon(surface, 'Blue', ((170,531), (89,531), (89,129), (411,129), (411,531), (330,531), (330,541), (421,541), (421, 119), (79,119), (79,541), (170,541)), 0)
#-------------------------------------------------------------------


#pieces
#-------------------------------------------------------------------
pieces = {}
class Pieces:
    #placing decide onde  peça  é colocada
    def draw_pieces_type1(surface, rectangles_center, placing):
        #surf_piece1 = pygame.surface.Surface((piece_sieze, piece_sieze))
        #piece1 = surf_piece1.get_rect(center = rectangles_center['rect11'])
        piece_sieze = 70
        
        if placing == {''}:
            pass
        else:
            for place in placing:
                key = 'rect' + str(place)
                x = rectangles_center[key][0] - 35 # a peça fica no centro do retângulo se não retirarmos 35 para recentrar 
                y = rectangles_center[key][1] - 35
                pygame.draw.rect(surface, 'Green', (x, y, piece_sieze, piece_sieze), 0)

    def moving_pieces():

        pass     
#-------------------------------------------------------------------
        

#main
#-------------------------------------------------------------------
#-------------------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background_surf,(0,0))
    screen.blit(level_background_surf,(0,0))
    screen.blit(level_surf, level_rect)
    screen.blit(board, (90,130))

    #activate board
    Board.draw_board(board, 5, 4, 80, rectangles_center)

    #activate boarder
    Board.draw_border(screen)

    #activate pieces type 1
    Pieces.draw_pieces_type1(board, rectangles_center, placing = {11, 12, 13, 14, 21, 23, 24, 31, 33, 34})


    pygame.display.update()
    
