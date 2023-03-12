import pygame
from model import Ball
from view import BallView
from controller import BallController

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

ball = Ball(50, 50, 20, 200, 20, 500)
ball_view = BallView(screen)
ball_controller = BallController(ball, ball_view)
ball_controller.run(30)
