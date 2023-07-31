import pygame
import random

# Initialize Pygame
import random

# Initialize Pygame
pygame.init()
import pygame
import random
import pygame
import pygame
import random

# Define colors
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define snake dimensions
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Initialize game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Add comments to improve readability and explain the purpose of each code block.

def draw_snake(snake_body):
    # Draw the snake on the window
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def generate_food():
    # Generate random coordinates for the food
    food_x = round(random.randrange(0, WINDOW_WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    food_y = round(random.randrange(0, WINDOW_HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    return food_x, food_y

def draw_food(food_x, food_y):
    # Draw the food on the window
    pygame.draw.rect(window, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

def display_score(score):
    # Display the current score on the window
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, BLACK)
    window.blit(text, (10, 10))

def game_over():
    # Display "Game Over" message on the window
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over", True, BLACK)
    window.blit(text, (WINDOW_WIDTH / 2 - text.get_width() / 2, WINDOW_HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.wait(2000)

def snake_game():
    # Initialize snake position and direction
    snake_x = WINDOW_WIDTH / 2
    snake_y = WINDOW_HEIGHT / 2
    snake_direction = "RIGHT"
    snake_body = []
    snake_length = 1

    # Initialize food position
    food_x, food_y = generate_food()

    # Initialize score
    score = 0

    # Game loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    snake_direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    snake_direction = "DOWN"

        # Move the snake
        if snake_direction == "LEFT":
            snake_x -= SNAKE_SPEED
        elif snake_direction == "RIGHT":
            snake_x += SNAKE_SPEED
        elif snake_direction == "UP":
            snake_y -= SNAKE_SPEED
        elif snake_direction == "DOWN":
            snake_y += SNAKE_SPEED

        # Check for game over conditions
        if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:

        # Check for game over conditions
        if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:
            game_over()
            break

        # Check if the snake has eaten the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = generate_food()
            score += 1
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = generate_food()
            score += 1
            snake_length += 1

        # Update snake body
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for snake self-collision
        if snake_head in snake_body[:-1]:
            game_over()
            break

        # Draw game objects
        window.fill(WHITE)
        draw_snake(snake_body)
        draw_food(food_x, food_y)
        display_score(score)
        pygame.display.update()

        # Set game frame rate
        clock.tick(15)

# Start the game
snake_game()