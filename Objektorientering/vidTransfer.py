from vidgear.gears import NetGear
from vidgear.gears import CamGear
from vidgear.gears.helper import reducer
import cv2
options = {
    "request_timeout": 5,
    "max_retries": 20,
}
class VideoStream():
    def __init__(self, source : int = 0, logging : bool = True, clientAddress : str = "192.168.4.1", port : str = "5454", framePercentage : int = 30) -> None:
        self.server = NetGear(logging=logging, address=clientAddress, port=port, **options)
        self.camera = CamGear(source=source, logging=logging).start()
        self.percentage = framePercentage

    def sendFrame(self):
        self.frame = self.camera.read()
        self.server.send(self.frame)
        cv2.imshow("Frame", self.frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            self.stop()
            cv2.destroyAllWindows()
            exit()
        #if self.frame is not None:
         #   self.frame = reducer(self.frame, self.percentage)
          #  self.server.send(self.frame)
    
    def stop(self):
        self.camera.stop()
        self.server.close()

    def __del__(self):
        self.camera.stop()
        self.server.close()


class VideoClient():
    def __init__(self, logging : bool = True, clientAddress : str = "192.168.4.1", port : str = "5454") -> None:
        self.client = NetGear(receive_mode=True, logging=logging, address=clientAddress, port=port, **options)
    
    def grabFrame(self):
        self.frame = self.client.recv()
        if self.frame is not None:
            return self.frame

    def stop(self):
        self.client.close()

    def __del__(self):
        self.client.close()