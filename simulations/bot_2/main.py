import pygame

# Initialize the pygame module
pygame.init()

# Set the dimensions of the screen
screen_width = 600
screen_height = 400

# Create a screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the color of the ball
ball_color = (255, 0, 0)

# Set the radius of the ball
ball_radius = 20

# Set the initial position of the ball
ball_x = 50
ball_y = 50

# Set the initial velocity of the ball
ball_dx = 5
ball_dy = 5

# Set the gravity
gravity = 0.1

# Set the game clock
clock = pygame.time.Clock()

# Loop until the user closes the window
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy
    ball_dy += gravity

    # Bounce the ball off the walls
    if ball_x > screen_width - ball_radius or ball_x < ball_radius:
        ball_dx *= -1
    if ball_y > screen_height - ball_radius or ball_y < ball_radius:
        ball_dy *= -1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(
        screen, ball_color, (int(ball_x), int(ball_y)), ball_radius
    )

    # Update the screen
    pygame.display.update()

    # Set the game clock speed
    clock.tick(60)
