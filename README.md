
**Hand Gesture Volume Control**

This project uses computer vision techniques to control the system volume based on hand gestures captured by a webcam. 
By tracking the position of specific landmarks on the hand, the program interprets gestures to increase or decrease the volume.

**Features:**

Track hand movements using the webcam

Calculate the length of a line drawn between two landmarks on the hand

Map the length to change the system volume range

Display the volume percentage on the video frame

Visualize the volume level using filled rectangles

Offer a real-time interactive volume control experience


**Prerequisites:**

Python 3.x

OpenCV library

NumPy library

pycaw library

Webcam connected to the computer

**Usage:**

Install the required libraries by running pip install opencv-python numpy pycaw.

Connect a webcam to your computer.

Run the script main.py.

Adjust the volume by moving your hand closer or farther from the webcam.

Observe the volume percentage and the visual representation of the volume level on the video frame.

