import pygame , random, sys

screen_width = 600
screen_height = 600

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

light_green = (0, 170, 140)
dark_green = (0, 140 , 120)
food_color = (250, 200, 0)
snake_color = (34, 34, 34)

up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range (0, int(grid_width)):
            if (x + y) % 2 == 0:
                light = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, light_green, light)
            else:
                dark = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, dark_green, dark)


def main():
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

        drawGrid(surface)
        screen.blit(surface, (0, 0))  # Yazi yazdir
        pygame.display.update()

main()

