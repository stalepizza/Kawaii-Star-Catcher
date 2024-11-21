import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kawaii Star Catcher")

# Clock
clock = pygame.time.Clock()

# Load assets
background = pygame.image.load("image.png")  # Load background image
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale to fit the screen
character = pygame.image.load("character.png")  # Your character sprite
character = pygame.transform.scale(character, (80, 80))
star = pygame.image.load("star.png")  # Your star sprite
star = pygame.transform.scale(star, (40, 40))

# Game variables
character_x, character_y = WIDTH // 2, HEIGHT - 100
character_speed = 8
star_x, star_y = random.randint(0, WIDTH - 40), -40
star_speed = 5
score = 0
missed = 0

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw the background image

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= character_speed
    if keys[pygame.K_RIGHT] and character_x < WIDTH - 80:
        character_x += character_speed

    # Star movement
    star_y += star_speed
    if star_y > HEIGHT:
        star_y = -40
        star_x = random.randint(0, WIDTH - 40)
        missed += 1

    # Collision detection
    if (character_x < star_x < character_x + 80 or character_x < star_x + 40 < character_x + 80) and \
            character_y < star_y + 40 < character_y + 80:
        score += 1
        star_y = -40
        star_x = random.randint(0, WIDTH - 40)

    # Draw elements
    screen.blit(character, (character_x, character_y))
    screen.blit(star, (star_x, star_y))

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    missed_text = font.render(f"Missed: {missed}/5", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))

    # Game over
    if missed >= 5:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
