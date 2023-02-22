import serial
import keyboard

# Connect to the serial port that the Arduino is using
# ser = serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial('/dev/rfcomm0', 9600)

# Define the key-to-command mappings
key_commands = {
    'up': '100_100\n',
    'down': '0_0\n',
    'left': '0_100\n',
    'right': '100_0\n'
}

# Keep reading keyboard input and sending corresponding motor commands
while True:
    if keyboard.is_pressed('esc'):
        break  # Stop the program when the 'ESC' key is pressed
    elif keyboard.is_pressed('up'):
        ser.write(key_commands['up'].encode())
    elif keyboard.is_pressed('down'):
        ser.write(key_commands['down'].encode())
    elif keyboard.is_pressed('left'):
        ser.write(key_commands['left'].encode())
    elif keyboard.is_pressed('right'):
        ser.write(key_commands['right'].encode())
