from simple_pid import PID
import pygame
import numpy as np


class pid_target:
    def __init__(self):
        self.PID = PID(0.5, 1, 0, setpoint=0)
        self.old_angular_speed = 0

    def target(self, target_position, robot):
        distance_to_target = np.linalg.norm(
            np.array(target_position) - robot.position)
        desired_orientation = np.arctan2(
            target_position[1] - robot.position[1],
            target_position[0] - robot.position[0],
        )

        error = (desired_orientation - robot.orientation +
                 np.pi) % (2 * np.pi) - np.pi

        angular_speed = np.degrees(self.PID(error))

        self.old_angular_speed = angular_speed
        linear_speed = 5 if distance_to_target > 10 else 0

        return linear_speed, angular_speed


def draw_bot(screen, color, diameter, position, orientation):
    end_point = position + diameter / 2 * np.array(
        [np.cos(orientation), np.sin(orientation)]
    )
    pygame.draw.circle(
        screen,
        color,
        position,
        diameter / 2,
    )
    pygame.draw.line(
        screen,
        "white",
        position,
        end_point,
    ),


def debug(text, position, bgcolor, fgcolor, screen):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(text, True, fgcolor, bgcolor)
    screen.blit(text, position)
