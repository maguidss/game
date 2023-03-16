import pygame 
from sys import exit 

#ecrã
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('PuzzlePacked IQ Games')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

#level button
level_surf = test_font.render('Level', False, 'White')
level_rect = level_surf.get_rect(center = (250, 50))
pygame.draw.rect(screen, 'Red', level_rect, 10)



while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(level_surf, level_rect)
    pygame.display.update()
    clock.tick(60)
