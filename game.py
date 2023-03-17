import pygame
from sys import exit
from board import*

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
board_surf = pygame.Surface((320, 400))
board_rect = board_surf.get_rect(midbottom = (250,530)) 

#-------------------------------------------------------------------

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surf,(0,0))
    screen.blit(level_background_surf,(0,0))
    screen.blit(level_surf, level_rect)
    

    #activate board
    screen.blit(board_surf, board_rect)
    GameBoard(ROWS, COLUMNS, BLOCK_SIZE).draw_board(board_surf)


    pygame.display.update()
    clock.tick(60)