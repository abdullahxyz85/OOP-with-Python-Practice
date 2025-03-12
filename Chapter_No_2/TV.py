# TV Class:
class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default lists of channels:
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM  # Integer divide
    def power(self):
        self.isOn = not self.isOn  # toggles
    def volumeUp(self):
        if not self.isOn:
            return 
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0
    def channelDown(self):
        if not self.isOn:
            return 
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
    def showInfo(self):
        print()
        print("TV Status")
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('   Volume is: ', self.volume, '(sound is muted)')
            else:
                print('     Volume is:', self.volume)
        else:
            print('     TV is: Off')

# Main Code:
oTV = TV()

# Turn the TV on and show the status:
oTV.power()
oTV.showInfo()

# Change the channel up twice, raise the volume twice and show the status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Turn the TV Off, show status, turn the TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Change the channel to ll, mute the sound, show the status 
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()