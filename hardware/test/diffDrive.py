import pygame
import serial
import threading
import numpy as np

# Set up Pygame window and fonts
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Robot Control')

ser = serial.Serial('/dev/rfcomm0', 9600)
theta, x, y, speed1, speed2 = 0, 0, 0, 0, 0
wheel_radius = 3.0  # in centimeters
wheel_distance = 10.0  # in centimeters
circle_radius = 5


def send_command(speed1, speed2):
    command = str(speed1) + ',' + str(speed2) + '\n'
    ser.write(command.encode())


def send_thread():
    global speed1, speed2
    while True:
        send_command(speed1, speed2)


threading.Thread(target=send_thread, daemon=True).start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed1, speed2 = 50, 50
            elif event.key == pygame.K_DOWN:
                speed1, speed2 = 0, 0
            elif event.key == pygame.K_LEFT:
                speed1, speed2 = 0, 50
            elif event.key == pygame.K_RIGHT:
                speed1, speed2 = 50, 0

    if ser.in_waiting > 0:
        data = ser.readline().decode().rstrip()
        distance1, distance2 = data.split(',')
        distance1, distance2 = int(
            float(distance2)/20), int(float(distance1)/20)
        delta_x = (distance1 + distance2) / 2.0 * np.cos(theta)
        delta_y = (distance1 + distance2) / 2.0 * np.sin(theta)
        delta_theta = (distance2 - distance1) / (2.0 * wheel_distance)
        x += delta_x
        y += delta_y
        theta += delta_theta

    screen.fill((255, 255, 255))
    text1 = font.render(str(speed1) + '_' + str(speed2), True, (0, 0, 0))
    screen.blit(text1, (10, 10))
    circle_x = int(x) + 200
    circle_y = int(y) + 200
    pygame.draw.circle(screen, (0, 0, 255),
                       (circle_x, circle_y), circle_radius)
    pygame.display.update()

pygame.quit()
ser.close()
