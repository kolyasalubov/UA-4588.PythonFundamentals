import pygame

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Boundaries")

rect_width, rect_height = 100, 80
rect_x, rect_y = 200, 150
rect_speed = 5


rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect.x += rect_speed
    if keys[pygame.K_UP]:
        rect.y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect.y += rect_speed

    
    if rect.x < 0:
        rect.x = 0
    if rect.y < 0:
        rect.y = 0
    if rect.x + rect.width > WIDTH:
        rect.x = WIDTH - rect.width
    if rect.y + rect.height > HEIGHT:
        rect.y = HEIGHT - rect.height

    
    screen.fill((255, 255, 255))  
    pygame.draw.rect(screen, (0, 0, 255), rect)  
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
