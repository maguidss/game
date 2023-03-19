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
level_rect = level_surf.get_rect(center = (250, 50))
pygame.draw.rect(screen, 'Red', level_rect, 10)



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