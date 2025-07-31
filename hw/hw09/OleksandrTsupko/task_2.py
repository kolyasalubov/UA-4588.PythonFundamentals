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
    
    if keys[pygame.K_LEFT]:
        COORD_X = (COORD_X[0] - DELTA_STEP, COORD_X[1])
        COORD_Y = (COORD_Y[0] - DELTA_STEP, COORD_Y[1])
        COORD_Z = (COORD_Z[0] - DELTA_STEP, COORD_Z[1])
    if keys[pygame.K_RIGHT]:
        COORD_X = (COORD_X[0] + DELTA_STEP, COORD_X[1])
        COORD_Y = (COORD_Y[0] + DELTA_STEP, COORD_Y[1])
        COORD_Z = (COORD_Z[0] + DELTA_STEP, COORD_Z[1])
    if keys[pygame.K_UP]:
        COORD_X = (COORD_X[0], COORD_X[1] - DELTA_STEP)
        COORD_Y = (COORD_Y[0], COORD_Y[1] - DELTA_STEP)
        COORD_Z = (COORD_Z[0], COORD_Z[1] - DELTA_STEP)
    if keys[pygame.K_DOWN]:
        COORD_X = (COORD_X[0], COORD_X[1] + DELTA_STEP)
        COORD_Y = (COORD_Y[0], COORD_Y[1] + DELTA_STEP)
        COORD_Z = (COORD_Z[0], COORD_Z[1] + DELTA_STEP)

    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.polygon(gameDisplay, RED_COLOR, [COORD_X,COORD_Y,COORD_Z])
    pygame.display.update()
    clock.tick(FPS)
    