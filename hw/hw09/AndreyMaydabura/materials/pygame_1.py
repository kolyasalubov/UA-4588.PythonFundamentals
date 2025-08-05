import pygame

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WIDTH_DISPLAY = 640
HEIGHT_DISPLAY = 400

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)

# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((600, 400))

# gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

# gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("My first game")


done = True
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.draw.rect(gameDisplay, ORANGE, [55, 50, 80, 55])

    pygame.display.update()
    clock.tick(FPS)
