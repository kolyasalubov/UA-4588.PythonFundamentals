import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = (200, 100)
COORD_Y = (100, 300)
COORD_Z = (300, 300)

DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    shift_x = 0
    shift_y = 0

    if keys[pygame.K_LEFT]:
        shift_x = -DELTA_STEP
    if keys[pygame.K_RIGHT]:
        shift_x = DELTA_STEP
    if keys[pygame.K_UP]:
        shift_y = -DELTA_STEP
    if keys[pygame.K_DOWN]:
        shift_y = DELTA_STEP

    if (
        COORD_X[0] + shift_x < 0 or 
        COORD_Y[0] + shift_x < 0 or 
        COORD_Z[0] + shift_x < 0 or
        COORD_X[0] + shift_x > WIDTH_DISPLAY or
        COORD_Y[0] + shift_x > WIDTH_DISPLAY or
        COORD_Z[0] + shift_x > WIDTH_DISPLAY
    ):
        shift_x = 0

    if (
        COORD_X[1] + shift_y < 0 or 
        COORD_Y[1] + shift_y < 0 or 
        COORD_Z[1] + shift_y < 0 or
        COORD_X[1] + shift_y > HEIGHT_DISPLAY or
        COORD_Y[1] + shift_y > HEIGHT_DISPLAY or
        COORD_Z[1] + shift_y > HEIGHT_DISPLAY
    ):
        shift_y = 0

    COORD_X = (COORD_X[0] + shift_x, COORD_X[1] + shift_y)
    COORD_Y = (COORD_Y[0] + shift_x, COORD_Y[1] + shift_y)
    COORD_Z = (COORD_Z[0] + shift_x, COORD_Z[1] + shift_y)



    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.polygon(gameDisplay, RED_COLOR, [COORD_X,COORD_Y,COORD_Z])
    pygame.display.update()
    clock.tick(FPS)
    