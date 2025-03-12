# Procedural light switch 
def turnOn():
    #global variable is used to repsresent the state
    global switchIsOn
    #turn the light on
    switchIsOn = True
def turnOff():
    #global variable is used to repsresent the state
    global switchIsOn
    #turn the light off
    switchIsOn = False
#  Main Code:
switchIsOn = False  # a global Boolean

#Test Code:
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
