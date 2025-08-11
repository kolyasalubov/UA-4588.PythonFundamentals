import pygame


FPS = 60

WIDTH_DISPLAY= 500
HEIGHT_DISPLAY=500

COORD_X=225
COORD_Y=225

WIDTH_RECTANGLE=50
HEIGHT_RECTANGLE=50

DELTA_STEP=5

IVORY3_COLOUR = pygame.Color('ivory3')
SEAGREEN4_COLOR = pygame.Color('seagreen4')

pygame.init()


# gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first pygame program")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    screen = pygame.display.get_surface()
    
    WIDTH_DISPLAY=screen.get_width()
    HEIGHT_DISPLAY=screen.get_height()

    keys = pygame.key.get_pressed()
    pygame.display.update()
    
    if keys[pygame.K_LEFT] and COORD_X >= DELTA_STEP:
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X + DELTA_STEP <= WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y >= DELTA_STEP:
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y + DELTA_STEP <= HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y = COORD_Y+DELTA_STEP


    gameDisplay.fill(IVORY3_COLOUR) 

    pygame.draw.rect(gameDisplay, SEAGREEN4_COLOR, [COORD_X, COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
