import cv2
import numpy as np
import HandModule as hm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
purple = (255, 0, 255)

img = cv2.imread("C:/Users/Mehrdad/PycharmProjects/PCvol/vol.jpg")
if img is None:
    print("Failed to load the image.")
else:
    height, width = img.shape[:2]
    if height >= 40 and width >= 40:
        img = cv2.resize(img, (40, 40))
        # Rest of the code
    else:
        print("Image dimensions are too small for resizing.")

width, height = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
detector = hm.Detector(detectionCon=0.85)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()
minvol = volRange[0]
maxvol = volRange[1]

volper=0
volrec=400                  #mabda nist

while True:
    _, frame = cap.read()
    frame = detector.findHands(frame)
    img_resized = cv2.resize(img, (50, 50))
    frame[height - 50:height, 0:50] = img_resized
    landmarkList = detector.Position(frame, draw=False)
    if len(landmarkList) != 0:
        # print(landmarkList[4],landmarkList[8])
        x1, y1 = landmarkList[4][1], landmarkList[4][2]
        x2, y2 = landmarkList[8][1], landmarkList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(frame, (x1, y1), 10, purple, -1)
        cv2.circle(frame, (x2, y2), 10, purple, -1)
        cv2.line(frame, (x1, y1), (x2, y2), purple, 3)
        cv2.circle(frame, (cx, cy), 10, purple, -1)
        length = np.hypot(x2 - x1, y2 - y1)
        # length      #10-215
        # volRange       -65    0
        # per             0-100
        vol = np.interp(length, [10, 215], [minvol, maxvol])
        volper= np.interp(length,[10,215],[0,100])
        volrec=np.interp(length,[10  ,215],[420, 180])
        # print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length < 20:
            cv2.circle(frame, (cx, cy), 10, green, -1)
        if length > 150:
            cv2.circle(frame, (cx, cy), 10, blue, -1)
    cv2.putText(frame,f'{int(volper)}%',(150,450),cv2.FONT_HERSHEY_COMPLEX,1,green,3)

    interval= int(np.interp(volrec ,[180,420] , [5,0]))
    print(interval)
    for i in range(0, interval):
        x1 = int(95 + 10*i)
        y1 = int(400-20*i)
        x2 = int(100+10*i)
        y2 = 440
        cv2.rectangle(frame,(x1,y1), (x2,y2), green, -1)
    cv2.imshow('webcam', frame)
    cv2.waitKey(1)
