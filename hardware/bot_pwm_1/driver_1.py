import pygame
import serial
import threading

pygame.init()

win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

ser = serial.Serial("/dev/rfcomm0", 9600, timeout=0)

ser_lock = threading.Lock()

black = (0, 0, 0)
white = (255, 255, 255)

left_motor = 0
right_motor = 0
running = True


def send_motor_commands():
    while running:
        ser_lock.acquire()

        command = "{:d}_{:d}\n".format(left_motor, right_motor)
        ser.write(command.encode())

        ser_lock.release()


motor_thread = threading.Thread(target=send_motor_commands)
motor_thread.start()

clock = pygame.time.Clock()

while running:
    clock.tick(60)

    serial_data = ser.readline().decode().strip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                left_motor = 100
                right_motor = 100
            elif event.key == pygame.K_DOWN:
                left_motor = 0
                right_motor = 0
            elif event.key == pygame.K_LEFT:
                left_motor = 0
                right_motor = 100
            elif event.key == pygame.K_RIGHT:
                left_motor = 100
                right_motor = 0

    win.fill(black)

    font = pygame.font.Font(None, 36)
    text = font.render(serial_data, True, white)
    text_rect = text.get_rect(center=(win_width / 2, win_height / 2))
    win.blit(text, text_rect)

    pygame.display.update()

motor_thread.join()

ser.close()

pygame.quit()
