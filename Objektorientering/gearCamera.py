from vidgear.gears import CamGear

class Camera():
    def __init__(self, source: int = 0, logging: bool = True) -> None:
        self.camera = CamGear(source = source, logging = logging).start()

    def grabFrame(self):
        self.frame = self.camera.read()
        if self.frame is not None:
            return self.frame
    
    def stop(self):
        print("Tvunget STOP")
        self.camera.stop()

    def __del__(self):
        print("STOP")
        self.camera.stop()
