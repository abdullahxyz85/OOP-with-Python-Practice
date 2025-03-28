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

# Main Code:
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Dimmer 2:
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Dimmer3:
oDimmer3 = DimmerSwitch('Dimmer3')

# Ask each switch to show itself:
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()

# oDimmer = DimmerSwitch()
# oDimmer.turnOn()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.show()
# # Lower the level:
# oDimmer.lowerLevel()
# oDimmer.lowerLevel()
# oDimmer.turnOff()
# oDimmer.show()
# # Turn the switch on and raise the level:
# oDimmer.turnOn()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.raiseLevel()
# oDimmer.show()