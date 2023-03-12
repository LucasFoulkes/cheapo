import pygame
import numpy as np
from simple_pid import PID


def orient(p1, p2):
    return np.arctan2(p2[1] - p1[1], p2[0] - p1[0])


def err(d, c):
    return (d - c + np.pi) % (2 * np.pi) - np.pi


def dist(p1, p2):
    return np.linalg.norm(p1 - p2)


class PidCtrl:
    def __init__(self, robot):
        self.pid = PID(0.5, 1, 0, setpoint=0)
        self.robot = robot

    def get_speed(self, target):
        d = dist(target, self.robot.position)
        o = orient(self.robot.position, target)
        e = err(o, self.robot.orientation)
        a = np.degrees(self.pid(e))
        l = 20 if d > 50 else 0
        return l, a


class BangBangCtrl:
    def __init__(self, robot):
        self.robot = robot

    def get_speed(self, target):
        d = dist(target, self.robot.position)
        o = orient(self.robot.position, target)
        e = err(o, self.robot.orientation)
        if e > -0.1 and e < 0.1:
            a = 0
        elif e > 0:
            a = -0.5
        else:
            a = 0.5
        l = 20 if d > 50 else 0
        print(l, a)
        return l, a


def draw_bot(r, c):
    ep = r.position + r.wheel_separation / 2 * np.array(
        [np.cos(r.orientation), np.sin(r.orientation)]
    )
    pygame.draw.circle(r.screen, c, r.position, r.wheel_separation // 2)
    pygame.draw.line(r.screen, "white", r.position, ep)


def debug(t, p, bg, fg, screen):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(t, True, fg, bg)
    screen.blit(text, p)
