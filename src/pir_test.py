import RPi.GPIO as GPIO
import time

# Set up GPIO
PIR_PIN = 27
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)  # Give time for the PIR sensor to settle
    print("Ready")

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
        else:
            print("No motion")
        time.sleep(1)

except KeyboardInterrupt:
    print("Quit")
finally:
    GPIO.cleanup()
