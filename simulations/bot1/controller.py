import numpy as np
import pygame
import copy
import utils

targeting_algorithm = utils.pid_target()


class Controller:
    def __init__(self, robot):
        self.position = copy.copy(robot.position)
        self.orientation = copy.copy(robot.orientation)
        self.screen = pygame.display.get_surface()
        self.robot = robot
        self.old_left_ticks = 0
        self.old_right_ticks = 0
        self.max_speed = 5

    def target(self):
        target_position = pygame.mouse.get_pos()
        linear_speed, angular_speed = targeting_algorithm.target(
            target_position, self
        )
        self.diff_drive(linear_speed, angular_speed)

    def diff_drive(self, linear_speed, angular_speed):
        angular_speed = np.radians(angular_speed)
        left_speed = (
            linear_speed - 0.5 * angular_speed * self.robot.wheel_separation
        )
        right_speed = (
            linear_speed + 0.5 * angular_speed * self.robot.wheel_separation
        )
        left_speed, right_speed = np.round(left_speed, 2), np.round(
            right_speed, 2
        )
        left_speed = max(-self.max_speed, min(left_speed, self.max_speed))
        right_speed = max(-self.max_speed, min(right_speed, self.max_speed))
        utils.debug(
            f"L_{left_speed}_R_{right_speed}",
            [
                self.position[0] + self.robot.wheel_separation / 2,
                self.position[1],
            ],
            "white",
            "black",
            self.screen,
        )
        self.robot.move(left_speed, right_speed)
        self.update_pose()

    def update_pose(self):
        new_ticks = self.robot.get_ticks_count()
        left_delta_ticks = new_ticks[0] - self.old_left_ticks
        right_delta_ticks = new_ticks[1] - self.old_right_ticks
        self.old_left_ticks, self.old_right_ticks = new_ticks

        left_distance = (
            left_delta_ticks / 20 * self.robot.wheel_radius * 2 * np.pi
        )
        right_distance = (
            right_delta_ticks / 20 * self.robot.wheel_radius * 2 * np.pi
        )

        linear_speed = (left_distance + right_distance) / 2
        angular_speed = (
            left_distance - right_distance
        ) / self.robot.wheel_separation

        self.orientation += angular_speed
        self.position += np.array(
            [
                linear_speed * np.cos(self.orientation),
                linear_speed * np.sin(self.orientation),
            ]
        )
        utils.draw_bot(
            self.screen,
            "grey",
            self.robot.wheel_separation,
            self.position,
            self.orientation,
        )

    def reset(self):
        self.robot.reset()
        self.position = [400.0, 300.0]
        self.orientation = 0.0
        self.old_left_ticks = 0
        self.old_right_ticks = 0
