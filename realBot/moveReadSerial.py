import pygame
import serial
import threading

# Initialize Pygame
pygame.init()

# Set up the Pygame window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

# Set up the serial port
ser = serial.Serial('/dev/rfcomm0', 9600, timeout=0)

# Set up a lock for the serial port to prevent conflicts
ser_lock = threading.Lock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the main game loop
left_motor = 0
right_motor = 0
running = True

# Define a function to send motor commands in a separate thread


def send_motor_commands():
    while running:
        # Acquire the lock on the serial port
        ser_lock.acquire()

        # Send the motor commands to the serial port
        command = "{:d}_{:d}\n".format(left_motor, right_motor)
        ser.write(command.encode())

        # Release the lock on the serial port
        ser_lock.release()


# Start the thread to send motor commands
motor_thread = threading.Thread(target=send_motor_commands)
motor_thread.start()

# Set up a clock to limit the read/write operations to 60 times per second
clock = pygame.time.Clock()

while running:
    # Limit the loop to 60 times per second
    clock.tick(60)

    # Read the serial data
    serial_data = ser.readline().decode().strip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          # Handle keypress events to control the robot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move the robot forward
                left_motor = 100
                right_motor = 100
            elif event.key == pygame.K_DOWN:
                # Move the robot backward
                left_motor = 0
                right_motor = 0
            elif event.key == pygame.K_LEFT:
                # Turn the robot left
                left_motor = 0
                right_motor = 100
            elif event.key == pygame.K_RIGHT:
                # Turn the robot right
                left_motor = 100
                right_motor = 0

    # Clear the screen
    win.fill(black)

    # Display the serial data on the Pygame screen
    font = pygame.font.Font(None, 36)
    text = font.render(serial_data, True, white)
    text_rect = text.get_rect(center=(win_width/2, win_height/2))
    win.blit(text, text_rect)

    # Update the screen
    pygame.display.update()

# Stop the thread to send motor commands
motor_thread.join()

# Close the serial port
ser.close()

# Quit Pygame
pygame.quit()
