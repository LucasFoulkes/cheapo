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
        self.left_ticks_count = 0
        self.right_ticks_count = 0

    def move(self, left_degrees, right_degrees):
        left_distance = left_degrees * self.wheel_radius * np.pi / 180
        right_distance = right_degrees * self.wheel_radius * np.pi / 180

        self.update_pose(left_distance, right_distance)

        utils.draw_bot(
            self.screen,
            "black",
            self.wheel_separation,
            self.position,
            self.orientation,
        )

    def get_ticks_count(self):
        return int(self.left_ticks_count * 20), int(
            self.right_ticks_count * 20
        )

    def reset(self):
        self.left_ticks_count = 0
        self.right_ticks_count = 0
        self.position = [400.0, 300.0]
        self.orientation = 0

    def update_pose(self, left_distance, right_distance):
        linear_speed = (self.wheel_radius / 2) * (
            left_distance + right_distance
        )
        angular_speed = (self.wheel_radius / self.wheel_separation) * (
            left_distance - right_distance
        )

        self.orientation += angular_speed
        self.position += linear_speed * np.array(
            [np.cos(self.orientation), np.sin(self.orientation)]
        )

        self.left_ticks_count += left_distance / (np.pi * 2)
        self.right_ticks_count += right_distance / (np.pi * 2)
