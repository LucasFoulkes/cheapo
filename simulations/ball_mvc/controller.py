import pygame


class BallController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self, fps):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            dt = 1 / fps
            self.model.update(
                dt, self.view.screen.get_width(), self.view.screen.get_height()
            )
            self.view.render(self.model)

            clock.tick(fps)
