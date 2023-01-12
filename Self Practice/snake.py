
import pygame
import random

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the dimensions of the snake and food blocks
block_size = 10

# Set the initial position of the snake
snake_pos = [250, 250]

# Set the initial direction of the snake
snake_dir = 'right'

# Set the initial snake body
snake_body = [[250, 250], [240, 250], [230, 250]]

# Set the initial position of the food
food_pos = [random.randrange(1, screen_width//block_size) * block_size,
            random.randrange(1, screen_height//block_size) * block_size]
food_spawn = True

# Set the score to 0
score = 0

# Set the font for the score
font = pygame.font.SysFont(None, 30)

# Set the FPS clock
clock = pygame.time.Clock()

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the game over flag to False
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = 'up'
            if event.key == pygame.K_DOWN:
                snake_dir = 'down'
            if event.key == pygame.K_LEFT:
                snake_dir = 'left'
            if event.key == pygame.K_RIGHT:
                snake_dir = 'right'

    # Update the position of the snake
    if snake_dir == 'up':
        snake_pos[1] -= block_size
    if snake_dir == 'down':
        snake_pos[1] += block_size
    if snake_dir == 'left':
        snake_pos[0] -= block_size
    if snake_dir == 'right':
        snake_pos[0] += block_size

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, screen_width//block_size) * block_size,
                    random.randrange(1, screen_height//block_size) * block_size]
   
