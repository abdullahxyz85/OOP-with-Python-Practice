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

# Create three DimmerSwitch Objects:
oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print("oDimmer1 variables:", vars(oDimmer1))
print()
oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
oDimmer3 = DimmerSwitch('Dimmer3')
print(type)