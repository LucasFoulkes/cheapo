import pygame
import numpy as np
from robot import Robot
from controller import Controller


class Game:
    def __init__(self, size):
        self.size = np.array(size)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

        self.robot = Robot(self.size / 2, 0, 5, 20)
        self.controller = Controller(self.robot)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False
        if (
            pygame.key.get_pressed()[pygame.K_SPACE]
            or self.robot.position[0] > self.size[0]
            or self.robot.position[0] < 0
            or self.robot.position[1] < 0
            or self.robot.position[1] > self.size[1]
        ):
            self.controller.reset()

    def run(self):
        while self.running:

            self.handle_input()

            self.screen.fill((255, 255, 255))

            self.controller.target(pygame.mouse.get_pos())

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = Game([800, 600])
    game.run()
