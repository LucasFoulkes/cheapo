import pygame
from robot import Robot
from controller import Controller
import numpy as np


def inputHandler(key, controller, SIZE):

    if (
        key()[pygame.K_SPACE]
        or controller.position[0] > SIZE[0]
        or controller.position[0] < 0
        or controller.position[1] < 0
        or controller.position[1] > SIZE[1]
    ):
        controller.reset()


def main():
    SIZE = np.array([800, 600])

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    running = True

    robot = Robot(SIZE / 2, 0, 5, 20)
    controller = Controller(robot)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        inputHandler(pygame.key.get_pressed, controller, SIZE)

        screen.fill((255, 255, 255))

        controller.target()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
