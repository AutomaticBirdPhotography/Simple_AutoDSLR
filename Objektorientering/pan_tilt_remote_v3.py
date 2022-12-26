"""
V 1.0
"""
import joyinput as j
import vidTransfer as v
import GUIopenCv as G
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if enable_button.isClicked((x, y)):
            if enable_button.active: print("on")
            home_button.deactivate()
            joy_button.deactivate()

        elif joy_button.isClicked((x,y)):
            if joy_button.active: print("joy")
            home_button.deactivate()
            enable_button.deactivate()
        elif home_button.isClicked((x,y)):
            if home_button.active: print("hjem")
            enable_button.deactivate()
            joy_button.deactivate()

#joy = j.Controller()    #initier joysticken, denne venter til den er koblet til
#videoClient = v.VideoClient(clientAddress="192.168.10.185", port="1234")
state_button = G.button("X", "X", (50,400), 50, 50, (255,0,0), (255,0,0))
align_button = G.button("+", "+", (150, 400), 50, 50, (0,0,255), (255,255,255))
home_button = G.button("Hjem", "Hjem", (250, 400), 50, 50, (0,0,255), (255,255,255))
enable_button = G.button("ON", "OFF", (350, 400), 50, 50, (0,255,0), (255,0,0))
joy_button = G.button("Stop joy", "Start joy", (450, 400), 100, 50, (255,0,0), (0, 255, 0))
main = G.window("Frame", onMouse)
cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    frame2 = cv2.pyrDown(frame)
    frame = main.createMultiple(frame2, frame)
    enable_button.create(frame)
    align_button.create(frame)
    state_button.create(frame)
    home_button.create(frame)
    joy_button.create(frame)
    main.show(frame)
    if joy_button.active:
        #print(joy.getPosition())
        pass
        