import pygame
import serial

# Define the serial port and baud rate
port = "/dev/rfcomm0"  # Change this to the port used by your Arduino
baud = 9600

# Create a serial connection
ser = serial.Serial(port, baud)

# Define the screen size
screen_width = 640
screen_height = 480

# Initialize Pygame
pygame.init()

# Create the Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Main loop
while True:
    # Check for Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame and close the serial port
            pygame.quit()
            ser.close()
            quit()

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Convert the mouse position to motor speeds
    left_speed = int(100 * mouse_y / screen_height)
    right_speed = int(100 * (screen_width - mouse_x) / screen_width)

    # Send the motor commands to the robot
    command = "{:d}_{:d}\n".format(left_speed, right_speed)
    ser.write(command.encode())

    # Draw a circle at the current mouse position
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 10)
    pygame.display.flip()
