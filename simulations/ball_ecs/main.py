import pygame
from components import Ball
from entities import BallEntity
from systems import BallSystem

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

ball = Ball(50, 50, 20, 200, 20, 500)
ball_entity = BallEntity(ball)

ball_system = BallSystem([ball_entity], 1 / 30, screen_width, screen_height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    ball_system.update()

    screen.fill((255, 255, 255))
    pygame.draw.circle(
        screen, (255, 0, 0), (int(ball.x), int(ball.y)), ball.radius
    )

    pygame.display.update()
    clock.tick(30)
