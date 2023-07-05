
**Hand Gesture Volume Control**

This project uses computer vision techniques to control the system volume based on hand gestures captured by a webcam. 
By tracking the position of specific landmarks on the hand, the program interprets gestures to increase or decrease the volume.

**Features**

Tracks hand movements using the webcam

Calculates the length of a line drawn between two landmarks on the hand

Maps the length to the system volume range

Displays the volume percentage on the video frame

Visualizes the volume level using filled rectangles

Offers a real-time interactive volume control experience


**Prerequisites**

Python 3.x

OpenCV library

NumPy library

pycaw library

Webcam connected to the computer

**Usage**

Install the required libraries by running pip install opencv-python numpy pycaw.

Connect a webcam to your computer.

Run the script main.py.

Adjust the volume by moving your hand closer or farther from the webcam.

Observe the volume percentage and the visual representation of the volume level on the video frame.

