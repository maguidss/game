import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('PuzzlePacked IQ Games')
clock = pygame.time.Clock()

score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center = (400, 50))
level_surface = pygame.Surface((100,200))
pygame.draw.rect(screen, 'Red',level_surface )
#test_surface.fill('Red')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(test_surface, (200,100))
    pygame.display.update()
    clock.tick(60)
