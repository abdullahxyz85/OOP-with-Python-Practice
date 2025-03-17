# DimmerSwitch Class:
class DimmerSwitch():
    def __init__(self, lable):
        self.switchIsOn = False
        self.brightness = 0
        self.label = lable
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
    def show(self):
        print("Label:", self.label)
        print("Switch is On?", self.switchIsOn)
        print("Brightness is:", self.brightness)

# Create two DimmerSwitch objects:
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer2 = DimmerSwitch('Dimmer2')

# Tell oDimmer1 to raise its level
oDimmer1.raiseLevel()

# Tell oDimmer2 to raise its level
oDimmer2.raiseLevel()