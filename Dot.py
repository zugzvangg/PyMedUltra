class Dot:
    def __init__(self, pos, brightness=0):
        self.pos = pos
        self.brightness = brightness

    def getPos(self):
        return self.pos

    def getBrightness(self):
        return self.brightness

    def setPos(self, pos):
        self.pos = pos

    def setBrightness(self, brightness):
        self.brightness = brightness
