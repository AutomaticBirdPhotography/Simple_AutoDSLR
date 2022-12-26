import cv2, time


class Camera():
    def __init__(self, source: int, scale: int = 50) -> None:
        self.camera = cv2.VideoCapture(source)
        self.scale = scale

    def grab_frame(self):
        ret, RAWframe = self.camera.read()
        if RAWframe is not None:
            #self.frame = cv2.resize(RAWframe, (int(RAWframe.shape[1]*self.scale/100), int(RAWframe.shape[0]*self.scale/100)), interpolation=cv2.INTER_NEAREST)
            self.frame = cv2.pyrDown(RAWframe)
            return self.frame

    def show_frame(self):
        cv2.imshow("Frame", self.frame)        

    def __del__(self):
        cv2.destroyAllWindows()
        self.camera.release()
