import pygame

pygame.init()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

ball_color = (255, 0, 0)
ball_radius = 20
ball_x = 50
ball_y = 50
ball_dx = 20
ball_dy = 200

gravity = 500

fps = 30

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    dt = 1 / fps
    ball_y += ball_dy * dt
    ball_dy += gravity * dt

    if ball_x > screen_width - ball_radius or ball_x < ball_radius:
        ball_dx *= -1
        ball_x = max(ball_radius, min(screen_width - ball_radius, ball_x))
    if ball_y > screen_height - ball_radius or ball_y < ball_radius:
        ball_dy *= -0.8 if ball_y > screen_height - ball_radius else -1
        ball_dx *= 0.8 if ball_y > screen_height - ball_radius else 1
        ball_y = max(ball_radius, min(screen_height - ball_radius, ball_y))

    screen.fill((255, 255, 255))
    pygame.draw.circle(
        screen, ball_color, (int(ball_x), int(ball_y)), ball_radius
    )

    pygame.display.update()
    clock.tick(fps)
