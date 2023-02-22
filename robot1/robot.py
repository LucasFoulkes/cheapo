import numpy as np
import pygame
import utils


class Robot:
    def __init__(self, position, orientation, wheel_radius, wheel_separation):
        self.screen = pygame.display.get_surface()
        self.position = position
        self.orientation = orientation
        self.wheel_radius = wheel_radius
        self.wheel_separation = wheel_separation

    def move(self, left_degrees, right_degrees):
        l_speed = left_degrees * self.wheel_radius * 2 * np.pi / 360
        r_speed = right_degrees * self.wheel_radius * 2 * np.pi / 360

        self.update_pose(l_speed, r_speed)

    def reset(self):
        self.position = [400.0, 300.0]
        self.orientation = 0

    def update_pose(self, l_speed, r_speed):
        linear_speed = (l_speed + r_speed) / 2
        angular_speed = (r_speed - l_speed) / (self.wheel_separation)
        self.orientation += angular_speed
        self.position += linear_speed * np.array(
            [np.cos(self.orientation), np.sin(self.orientation)]
        )
        utils.draw_bot(self, "black")
