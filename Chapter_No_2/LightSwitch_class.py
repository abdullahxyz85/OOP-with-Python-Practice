# oo_LightSwitch
class LightSwitch(): # parenthesis use after the class name is optional
    def __init__(self):
        self.switchIsOn = False
    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True
    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False
# To create a lightSwitch object form our lightSwitch class, we typically use like this:
oLightSwitch = LightSwitch()
# We would say that LightSwitch object is an instance of LightSwitch Class

# Instantiation:
# The process of creating an object from a class
class MyClass():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count + 1
        print(self.count)
myclass = MyClass()
myclass.increment()