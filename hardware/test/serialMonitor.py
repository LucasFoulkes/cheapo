import serial

SERIAL_PORT = "/dev/rfcomm0"
BAUD_RATE = 9600
SERIAL_TIMEOUT = 0.1


def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=SERIAL_TIMEOUT)

    try:
        while True:
            # Wait until data is available on the serial por
            while ser.in_waiting == 0:
                pass
            # Read the message and split it by the underscore character
            message = ser.readline().decode().strip()
            print(f"Received message: {message!r}")
    except KeyboardInterrupt:
        ser.close()


if __name__ == "__main__":
    main()
