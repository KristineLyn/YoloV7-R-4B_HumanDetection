# Smart Home Security: Intruder Detection System

Welcome to the **Smart Home Security: Intruder Detection System** project! This intelligent home security solution combines the power of a Raspberry Pi, PIR motion sensors, and the YOLOv7 Machine Learning model to detect intruders accurately and efficiently. With this system, your home gains a vigilant virtual guard capable of identifying human presence and instantly notifying you via a connected mobile app.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## Overview

The Smart Home Security: Intruder Detection System is designed to enhance home security by leveraging real-time image processing and machine learning. When motion is detected by a PIR sensor, the system takes a snapshot and runs YOLOv7 object detection to determine if a person is present. If a human is detected, the system saves the image to Firebase Storage and sends a notification through Firebase Realtime Database to a mobile app built with Flutter. The mobile app provides real-time access to the image and alert notifications, allowing homeowners to stay informed about potential intrusions.

## Features

- **Human Detection**: Accurately identifies if a detected motion is due to human presence.
- **Automated Image Capture**: Takes a photo upon motion detection.
- **YOLOv7 Model Integration**: Leverages YOLOv7 for real-time, high-accuracy object detection.
- **Firebase Integration**: Stores detected images in Firebase Storage and sends real-time alerts via Firebase Realtime Database.
- **Mobile Notifications**: Sends real-time alerts to a connected Flutter mobile app.
- **User-Friendly Mobile Interface**: View images and receive notifications directly on a smartphone.

## Hardware Requirements

- **Raspberry Pi 4 Model B**: Serves as the main computing device to handle PIR sensor inputs, camera interactions, and YOLOv7 processing.
- **PIR Sensor**: Detects motion in the specified area.
- **Webcam**: Captures images for analysis when motion is detected.

## Software Requirements

- **Raspberry Pi OS**: The operating system for the Raspberry Pi.
- **Python 3**: Programming language for handling sensor data, image processing, and Firebase interactions.
- **YOLOv7 Model**: Machine learning model for real-time object detection.
- **Firebase**: Cloud platform to store images and send notifications.
- **Flutter**: Framework to build the mobile app for notifications and image viewing.
- **Libraries and Dependencies**:
  - `OpenCV` for image handling
  - `firebase_admin` for Firebase interaction
  - `TensorFlow` or `PyTorch` for YOLOv7 integration

## How It Works

1. **Motion Detection**:
   - The PIR sensor continuously monitors the surroundings. When it detects motion, it sends a signal to the Raspberry Pi.

2. **Image Capture and Processing**:
   - Upon receiving the signal, the Raspberry Pi activates the connected webcam to capture an image of the detected area.
   - This image is then processed by the YOLOv7 model to determine if a human is present.

3. **Decision Making and Notification**:
   - If the YOLOv7 model identifies a human, the Raspberry Pi proceeds to store the image in Firebase Storage.
   - Simultaneously, it sends a real-time notification through Firebase Realtime Database, including a reference to the saved image.

4. **Mobile App Alert**:
   - The connected mobile app (built with Flutter) fetches notifications and images from Firebase, displaying them in an organized interface.
   - Users receive instant alerts with visual evidence whenever a human presence is detected.

## Installation

### Raspberry Pi Setup

1. **Install Raspberry Pi OS** and set up the Raspberry Pi 4 Model B.
2. **Set up Python 3** and required dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install opencv-python firebase_admin tensorflow
   ```
3. **Download YOLOv7 Weights and Model Configuration**:
   - Obtain YOLOv7 weights and model configuration files. Place them in a known directory on the Raspberry Pi.

4. **Configure Firebase**:
   - Set up a Firebase project.
   - Enable Firebase Storage and Firebase Realtime Database.
   - Download the `firebase.json` config file and place it in the project directory.

5. **Connect PIR Sensor and Webcam**:
   - Connect the PIR sensor to a GPIO pin on the Raspberry Pi.
   - Attach a USB or Pi Camera module for image capture.

### Firebase Setup

1. **Firebase Realtime Database**:
   - Enable Realtime Database in your Firebase project to send notifications.
   
2. **Firebase Storage**:
   - Set up Firebase Storage to save captured images for later review.

### Mobile App Setup (Flutter)

1. **Flutter Setup**:
   - Install Flutter and set up a new Flutter project for the mobile app.
   - Integrate Firebase into your Flutter project using Firebase SDKs for Realtime Database and Storage.

2. **Firebase Configuration**:
   - Add Firebase configuration to the Flutter app to enable access to your Firebase project.

### Run the System

1. Start the Raspberry Pi script to initiate monitoring:
   ```bash
   python3 intruder_detection.py
   ```
2. Launch the Flutter app on your mobile device to start receiving notifications.

## Future Improvements

- **Face Recognition**: Add face recognition capabilities to differentiate between family members and unknown individuals.
- **Alert Level Customization**: Allow users to set custom alert levels based on motion sensitivity or specific times of the day.
- **Multi-Camera Support**: Expand the system to support multiple cameras for larger areas.
- **Data Analytics**: Integrate Firebase Analytics to analyze intrusion patterns and alert frequency.

## Contributing

Contributions are welcome! If you'd like to improve the project, feel free to open an issue or submit a pull request. Please ensure all changes align with the project’s objectives and maintain consistent documentation. I want to say thank you to all YoloV7 Dev and All YoloV7 Contributor to make my project happen.


---

Enjoy the peace of mind that comes with **Smart Home Security: Intruder Detection System** – a powerful, personalized security system designed to keep your home safe in real time!