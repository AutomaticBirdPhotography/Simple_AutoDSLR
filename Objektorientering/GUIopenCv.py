import cv2
import numpy as np
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
class window():
    def __init__(self, win_name : str, funciton_on_mouse) -> None:
        self.win_name = win_name
        cv2.namedWindow(self.win_name)
        cv2.setMouseCallback(self.win_name, funciton_on_mouse)

    def show(self, frame):
        cv2.imshow(self.win_name, frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord("q"):
            cv2.destroyAllWindows()
            exit()

    def createMultiple(self, leftFrame, rightFrame):
        Lheight, Lwidth, Lchannels = leftFrame.shape
        Rheight, Rwidth, Rchannels = rightFrame.shape
        result = np.zeros((max(Lheight, Rheight), Lwidth+Rwidth, Lchannels), dtype=np.uint8)
        leftFrame = cv2.filter2D(leftFrame, -1, kernel)
        result[:Lheight,:Lwidth] = leftFrame
        result[:Rheight, Lwidth:Lwidth+Rwidth] = rightFrame
        result = cv2.copyMakeBorder(result, 0,50,50,50, cv2.BORDER_CONSTANT, value=0)
        return result

class button():
    def __init__(self, active_text, deactive_text, start_point, width, height, active_color, deactive_color):
        self.start_point = start_point
        self.end_point = (start_point[0]+width, start_point[1]+height)
        self.active_color = active_color
        self.active_text = active_text
        self.deactive_text = deactive_text
        self.deactive_color = deactive_color

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 1
        self.fontThicknes = 1
        
        self.active = False
        

    def create(self, frame):
        self.frame = frame
        if self.active:
            self.textsize = cv2.getTextSize(self.active_text, self.font, self.fontScale, self.fontThicknes)[0]# finn størrelsen på teksten
            self.textX = int((((self.end_point[0]-self.start_point[0]) - self.textsize[0]) / 2)+self.start_point[0])
            self.textY = int((((self.end_point[1]-self.start_point[1]) + self.textsize[1]) / 2)+self.start_point[1])

            self.frame = cv2.rectangle(self.frame, self.start_point, self.end_point, self.active_color, -1)
            self.frame = cv2.putText(self.frame, self.active_text, (self.textX, self.textY), self.font, self.fontScale, (0,0,0), self.fontThicknes)
        else:
            self.textsize = cv2.getTextSize(self.deactive_text, self.font, self.fontScale, self.fontThicknes)[0]# finn størrelsen på teksten
            self.textX = int((((self.end_point[0]-self.start_point[0]) - self.textsize[0]) / 2)+self.start_point[0])
            self.textY = int((((self.end_point[1]-self.start_point[1]) + self.textsize[1]) / 2)+self.start_point[1])

            self.frame = cv2.rectangle(self.frame, self.start_point, self.end_point, self.deactive_color, -1)
            self.frame = cv2.putText(self.frame, self.deactive_text, (self.textX, self.textY), self.font, self.fontScale, (0,0,0), self.fontThicknes)


    def isClicked(self, mousePos):
        if ((mousePos[0] < self.end_point[0]) & (mousePos[0] > self.start_point[0]) & (mousePos[1] < self.end_point[1]) & (mousePos[1] > self.start_point[1])):
            self.active = not self.active
            self.create(self.frame)
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
    