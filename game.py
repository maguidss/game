import pygame 
from sys import exit 

#ecrã
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('PuzzlePacked IQ Games')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
background_surf = pygame.image.load('Images\_background.jpg').convert()



#level button
level_background_surf = pygame.Surface((500,60))
level_background_surf.fill('Blue')
level_surf = test_font.render('Level', False, 'White')
level_rect = level_surf.get_rect(center = (250, 30))
pygame.draw.rect(screen, 'Red', level_rect, 4)


#board 
board = []
square11_surf = pygame.Surface((80,80))
board.append(square11_surf)
square12_surf = pygame.Surface((80,80))
board.append(square12_surf)
square13_surf = pygame.Surface((80,80))
board.append(square13_surf)
square14_surf = pygame.Surface((80,80))
board.append(square14_surf)
square15_surf = pygame.Surface((80,80))
board.append(square15_surf)
square21_surf = pygame.Surface((80,80))
board.append(square21_surf)
square22_surf = pygame.Surface((80,80))
board.append(square22_surf)
square23_surf = pygame.Surface((80,80))
board.append(square23_surf)
square24_surf = pygame.Surface((80,80))
board.append(square24_surf)
square25_surf = pygame.Surface((80,80))
board.append(square25_surf)
square31_surf = pygame.Surface((80,80))
board.append(square31_surf)
square32_surf = pygame.Surface((80,80))
board.append(square32_surf)
square33_surf = pygame.Surface((80,80))
board.append(square33_surf)
square34_surf = pygame.Surface((80,80))
board.append(square34_surf)
square35_surf = pygame.Surface((80,80))
board.append(square35_surf)
square41_surf = pygame.Surface((80,80))
board.append(square41_surf)
square42_surf = pygame.Surface((80,80))
board.append(square42_surf)
square43_surf = pygame.Surface((80,80))
board.append(square43_surf)
square44_surf = pygame.Surface((80,80))
board.append(square44_surf)
square45_surf = pygame.Surface((80,80))
board.append(square45_surf)

#for i in range(1,6,1):
#    for j in range(1,6,1):
#        word = "square" + str(i) + str(j) + "_surf"
#        board.append(word)

#-------------------------------------------------------------------

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surf,(0,0))
    screen.blit(level_background_surf,(0,0))
    screen.blit(level_surf, level_rect)
    x = 0
    y = 0
    for k in board:
        screen.blit(k,(49 + x,130))
        x += 80
        y += 80

    pygame.display.update()
    clock.tick(60)
