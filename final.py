import RPi.GPIO as GPIO
import time
import cv2
import subprocess

# Set up GPIO
PIR_PIN = 27
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Initialize the webcam
cap = cv2.VideoCapture(0)

def take_picture():
    time.sleep(0.5)  # Allow the camera to warm up and adjust to lighting conditions

    # Flush the camera buffer
    for _ in range(5):
        ret, frame = cap.read()

    # Capture the actual frame
    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f'/home/raspi/Pictures/motion_{timestamp}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Picture saved as {filename}")

        # Run detect.py with the saved image
        command = f"python test.py --weights yolov7-tiny.pt --conf 0.50 --img-size 640 --classes 0 --source {filename}"
        subprocess.run(command, shell=True)
        print(f"Detection performed on {filename}")

        # Allow some time for the process to complete before capturing the next frame
        time.sleep(2)

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
