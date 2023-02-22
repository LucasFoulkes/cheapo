import pygame
import serial
import threading
import numpy as np

# Set up Pygame window and fonts
SIZE = np.array([800, 800])
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Robot Control")

ser = serial.Serial("/dev/rfcomm0", 9600)
theta, x, y, speed1, speed2 = 0, 0, 0, 0, 0
wheel_radius = 4.32
wheel_distance = 10  # in centimeters


def send_command(speed1, speed2):
    command = str(speed1) + "," + str(speed2) + "\n"
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

    if ser.in_waiting > 0:
        data = ser.readline().decode().rstrip()
        distance1, distance2 = data.split(",")
        distance1, distance2 = int(float(distance2) / 20), int(
            float(distance1) / 20
        )
        delta_x = (distance1 + distance2) / 2.0 * np.cos(theta)
        delta_y = (distance1 + distance2) / 2.0 * np.sin(theta)
        delta_theta = (distance2 - distance1) / (2.0 * wheel_distance)
        x += delta_x
        y += delta_y
        theta += delta_theta

    screen.fill("white")
    circle_x, circle_y = int(x) + SIZE[0] // 2, int(y) + SIZE[1] // 2
    start_point = np.array([circle_x, circle_y])
    end_point = start_point + wheel_distance * np.array(
        [np.cos(theta), np.sin(theta)]
    )
    pygame.draw.circle(screen, "black", (circle_x, circle_y), wheel_distance)
    pygame.draw.line(screen, "white", start_point, end_point)

    mouse_pos = np.array(pygame.mouse.get_pos())
    x_diff = mouse_pos[0] - circle_x
    y_diff = mouse_pos[1] - circle_y
    angle_to_mouse = np.arctan2(y_diff, x_diff)
    error = (angle_to_mouse - theta + np.pi) % (2 * np.pi) - np.pi

    distance2mouse = np.sqrt(x_diff**2 + y_diff**2)

    if distance2mouse < 50:
        speed1, speed2 = 0, 0
    elif abs(error) <= 0.2:
        speed1, speed2 = 50, 50
    elif error < 0:
        speed1, speed2 = 0, 50
    else:
        speed1, speed2 = 50, 0

    text1 = font.render(
        f"{speed1}_{speed2}_{error}_{distance2mouse}", True, (0, 0, 0)
    )

    screen.blit(text1, (10, 10))

    pygame.display.update()

pygame.quit()
ser.close()
