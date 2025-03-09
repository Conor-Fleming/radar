import smbus2
import time

bus = smbus2.SMBus(1)

# This seems to be the address that gives no IO errors...
DEVICE_ADDR = 0x2B


def read_sensor():
    try:
        # read data from sensor
        data = bus.read_i2c_block_data(DEVICE_ADDR, 0x00, 2)

        # testing conversion
        val = (data[0] << 8) | data[1]

        # do data processing here if needed
        #
        #

        return val
    except Exception as e:
        print(f"Error reading sensor: {e}")
        return None

def main():
    print("Starting sensor reading...")

    try:
        while True:
            value = read_sensor()
            if value is not None:
                print(f"Sensor reading: {value}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Program stopped by user")


if __name__ == "__main__":
    main()
