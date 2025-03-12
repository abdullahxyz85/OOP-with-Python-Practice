class LightSwitch():
    def __init__(self):
        self.switchIsOn = False  

    def turnOn(self):
        # Turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # Turn the switch off
        self.switchIsOn = False  

    def show(self):  # Adding the testing
        print(self.switchIsOn)

# Main Code:
oLightSwitch = LightSwitch()  # Create a light switch object

# Calls to methods
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
