from pygame import joystick
from time import sleep

disconnected = False

class Controller():
    def __init__(self):
        self.checkPad(self)

    def checkPad(self):
        joystick.quit()
        joystick.init()
        joystick_count = joystick.get_count()
        for i in range(joystick_count):
            self.joystick = joystick.Joystick(i)
            self.joystick.init()
        if not joystick_count:
            if not disconnected:
                print("Koble til joystick!")
                disconnected = True
            sleep(1)
            self.checkPad(self)
        else:
            disconnected = False

        
    
    def getPosition(self):
        return(self.joystick.get_axis(0)*100, self.joystick.get_axis(1)*100)

    def stop(self):
        joystick.quit()

    def __del__(self):
        joystick.quit()