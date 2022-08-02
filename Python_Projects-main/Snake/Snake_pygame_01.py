import pygame , random, sys

screen_width = 600
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))  # Ekran olustur
font = pygame.font.SysFont('arial', 20)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 0, 0))   #===> Arkayi kirmizi yaptik
    rect = pygame.Rect(100, 300, 200, 200)   #==>(100,300)(x,y) ,rectangle olustur 200x200
    pygame.draw.rect(screen, (255, 255, 255), rect) # Rectangle cizdir
    score_text = font.render('Score: 0', True, (0, 0, 0))  # Yazi tanimla
    screen.blit(score_text, (10, 10)) # Yazi yazdir

    pygame.display.update()


