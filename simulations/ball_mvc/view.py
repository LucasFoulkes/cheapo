import pygame


class BallView:
    def __init__(self, screen):
        self.screen = screen

    def render(self, ball):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(
            self.screen, (255, 0, 0), (int(ball.x), int(ball.y)), ball.radius
        )
        pygame.display.update()
