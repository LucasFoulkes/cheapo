import numpy as np
import pygame
import utils


class Controller:
    def __init__(self, robot):
        self.screen = pygame.display.get_surface()
        self.robot = robot
        self.max_speed = 20
        self.control = utils.BangBangCtrl(self.robot)
        # self.control = utils.PidCtrl(self.robot)

    def target(self, target):
        linear_speed, angular_speed = self.control.get_speed(target)
        self.diff_drive(linear_speed, angular_speed)

    def diff_drive(self, linear_speed, angular_speed):
        tmp = (angular_speed * self.robot.wheel_separation) / 2
        left_speed = linear_speed + tmp
        right_speed = linear_speed - tmp
        left_speed = max(-self.max_speed, min(left_speed, self.max_speed))
        right_speed = max(-self.max_speed, min(right_speed, self.max_speed))
        self.robot.move(left_speed, right_speed)

    def reset(self):
        self.robot.reset()
