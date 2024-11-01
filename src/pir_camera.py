import RPi.GPIO as GPIO
import time
import cv2

# Set up GPIO
PIR_PIN = 27
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Initialize the webcam
cap = cv2.VideoCapture(0)

last_picture_time = 0
picture_delay = 10  # Delay between pictures in seconds

def take_picture():
    global last_picture_time
    current_time = time.time()
    if current_time - last_picture_time >= picture_delay:
        time.sleep(1)
        ret, frame = cap.read()
        if ret:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f'/home/raspi/Pictures/motion_{timestamp}.jpg'
            cv2.imwrite(filename, frame)
            print(f"Picture saved as {filename}")
            last_picture_time = current_time

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)  # Give time for the PIR sensor to settle
    print("Ready")

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            take_picture()
        else:
            print("No motion")
        time.sleep(1)  # Check the PIR sensor state every second

except KeyboardInterrupt:
    print("Quit")
finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
