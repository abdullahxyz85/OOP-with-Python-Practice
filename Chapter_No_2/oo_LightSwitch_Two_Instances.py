# Creating multiple instances from one class
# oo_LightSwitch:
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def show(self):
        print(self.switchIsOn)

# Main Code:
# here i create two different instances with the same one class

oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()