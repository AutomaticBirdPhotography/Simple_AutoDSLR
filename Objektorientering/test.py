import cv2
import GUIopenCv as G
import numpy as np


cap = cv2.VideoCapture(0)
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if enable_button.isClicked((x, y)):
            if enable_button.active: print("on")
            home_button.deactivate()
        elif home_button.isClicked((x,y)):
            if home_button.active: print("hjem")
            enable_button.deactivate()
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", onMouse)
enable_button = G.button("ON", "OFF", (50,480), 70, 40, (255, 255, 255), (100,100,0))
home_button = G.button("Hjem", "Hjem", (150, 480), 70, 40, (255, 255, 255), (188,32,12))
ret, frame = cap.read()
frame2 = cv2.pyrDown(frame)
height1, width1, channels1 = frame.shape
height2, width2, channels2 = frame2.shape

while True:
    ret, frame = cap.read()
    frame2 = cv2.pyrDown(frame)
    result = np.zeros((max(height1, height2), width1+width2, channels1), dtype=np.uint8)
    result[:height1,:width1] = frame
    result[:height2, width1:width1+width2] = frame2
    result = cv2.copyMakeBorder(result, 0,50,50,50, cv2.BORDER_CONSTANT, value=0)
    enable_button.create(result)
    home_button.create(result)
    cv2.imshow("Frame", result)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cap.release()
