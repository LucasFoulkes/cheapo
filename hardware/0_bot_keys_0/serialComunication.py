import pygame
import serial
import sys
import time

arduino = serial.Serial("/dev/rfcomm0", 115200, timeout=1)

pygame.init()
display = pygame.display.set_mode((640, 480))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print("Keydown")
            if event.key == pygame.K_UP:
                command = "f"
            if event.key == pygame.K_DOWN:
                command = "b"
            if event.key == pygame.K_LEFT:
                command = "l"
            if event.key == pygame.K_RIGHT:
                command = "r"
            if event.key == pygame.K_SPACE:
                command = "s"
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            try:
                arduino.write(bytes(command, "utf-8"))
            except:
                print("Error")
                pass
        if event.type == pygame.KEYUP:
            print("Keyup")
            try:
                arduino.write(bytes("s", "utf-8"))
            except:
                print("Error")
                pass
    display.fill((0, 0, 0))
    pygame.display.flip()
