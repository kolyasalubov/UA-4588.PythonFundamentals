from random import randint
import pygame


pygame.init()

WIDHT = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('Guess the number')

font = pygame.font.SysFont(None, 40)

BLACK = (0,0,0)
RED = (255,0,0)

r_number = randint(0, 100)
w_number = ""
message = "Write the number (1 - 100)"
tri = 0
max_tri = 10
game_over = False

def text(text, y):
    txt_surface = font.render(text, True, RED)
    screen.blit(txt_surface, (20, y))

running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if w_number.isdigit():
                        num = int(w_number)
                        tri += 1
                        if num == r_number:
                            message = f"Congratulations. You guessed {r_number}"
                            game_over = True
                        elif num < r_number:
                            message = "Your number is less!"
                        else:
                            message = "You number is more!"
                        w_number = ""
                elif event.key == pygame.K_BACKSPACE:
                    w_number = w_number[:-1]
                elif event.unicode.isdigit():
                    w_number += event.unicode
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                r_number = randint(0, 100)
                w_number = ""
                message = "Write the number (1 - 100)"
                tri = 0
                game_over = False

    text(message, 100)
    text(f"You number: {w_number}", 150)
    text(f"Attempt: {tri}/{max_tri}", 200)

    if game_over:
        text("Press SPACE restart the game", 250)

    pygame.display.flip()

pygame.quit()
