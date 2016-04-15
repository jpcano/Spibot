from webiopi.devices.serial import Serial

class PololuQik (object):
    def __init__ (self, deviceID, baudrate = 38400):
        self.uart =  Serial("ttyAMA0", baudrate)
        self.deviceID = deviceID

    def __write (self, data):
        self.uart.write((bytes('\xAA' + self.deviceID
                               + data, 'latin1')))
        
    def __setMotorSpeed (self, forwardcom, reversecom, speed):
        reverse = False
        if speed < 0:
            speed = -speed
            reverse = True
        if speed > 127:
            speed = 127
        if reverse:
            self.__write(reversecom + '%c' % speed)
        else:
            self.__write(forwardcom + '%c' % speed)

    def setM0Speed (self, speed):
        self.__setMotorSpeed('\x08', '\x0A', speed)

    def setM1Speed (self, speed):
        self.__setMotorSpeed('\x0C', '\x0E', speed)

    def setSpeeds (self, speed):
        self.setM0Speed(speed)
        self.setM1Speed(speed)
        
    def setM0Coast (self):
        self.__write('\x06')

    def setM1Coast (self):
        self.__write('\x07')

    def setCoasts (self):
        self.setM0Coast()
        self.setM1Coast()

    def setM0Brake (self):
        self.__write('\x08\x00')

    def setM1Brake (self):
        self.__write('\x0C\x00')

    def setBrakes (self):
        self.setM0Brake()
        self.setM1Brake()
        
    def getErrors (self):
        self.__write('\x02')

class FourWheelBot (object):
    def __init__ (self, speed=64, rotSpeed=64, turnSpeedRatio=0.5):
        self.fwheels = PololuQik('\x09')
        self.bwheels = PololuQik('\x0A')
        self.speed = speed
        self.rotSpeed = rotSpeed
        self.turnSpeedRatio = turnSpeedRatio
        self.__updateTurnSpeed(self.turnSpeedRatio)
        self.state = None
        self.fwheels.getErrors()
        self.bwheels.getErrors()

    def fl (self):
        self.fwheels.setM0Speed(self.turnSpeed)
        self.fwheels.setM1Speed(self.speed)
        self.bwheels.setM0Speed(self.turnSpeed)
        self.bwheels.setM1Speed(self.speed)
        self.state = self.fl

    def f (self):
        self.fwheels.setSpeeds(self.speed)
        self.bwheels.setSpeeds(self.speed)
        self.state = self.f

    def fr (self):
        self.fwheels.setM0Speed(self.speed)
        self.fwheels.setM1Speed(self.turnSpeed)
        self.bwheels.setM0Speed(self.speed)
        self.bwheels.setM1Speed(self.turnSpeed)
        self.state = self.fr

    def l (self):
        self.fwheels.setM0Speed(-self.rotSpeed)
        self.fwheels.setM1Speed(self.rotSpeed)
        self.bwheels.setM0Speed(-self.rotSpeed)
        self.bwheels.setM1Speed(self.rotSpeed)
        self.state = self.l
        
    def r (self):
        self.fwheels.setM0Speed(self.rotSpeed)
        self.fwheels.setM1Speed(-self.rotSpeed)
        self.bwheels.setM0Speed(self.rotSpeed)
        self.bwheels.setM1Speed(-self.rotSpeed)
        self.state = self.r

    def bl (self):
        self.fwheels.setM0Speed(-self.speed)
        self.fwheels.setM1Speed(-self.turnSpeed)
        self.bwheels.setM0Speed(-self.speed)
        self.bwheels.setM1Speed(-self.turnSpeed)
        self.state = self.bl

    def b (self):
        self.fwheels.setSpeeds(-self.speed)
        self.bwheels.setSpeeds(-self.speed)
        self.state = self.b

    def br (self):
        self.fwheels.setM0Speed(-self.turnSpeed)
        self.fwheels.setM1Speed(-self.speed)
        self.bwheels.setM0Speed(-self.turnSpeed)
        self.bwheels.setM1Speed(-self.speed)
        self.state = self.br
        
    def setCoast (self):
        self.fwheels.setCoasts()
        self.bwheels.setCoasts() 
        self.state = self.setCoast

    def setBrake (self):
        self.fwheels.setBrakes()
        self.bwheels.setBrakes() 
        self.state = self.setBrake

    def __updateTurnSpeed (self, ratio):
        self.turnSpeed = int(round((1 - ratio) * self.speed))

    def setSpeed (self, speed):
        if speed >=0 and speed < 128:
            self.speed = speed
            if self.state in [self.f, self.b,
                              self.fl, self.fr, self.bl, self.br]:
                self.__updateTurnSpeed(self.turnSpeedRatio)
                self.state()

    def setTurnSpeed (self, ratio):
        if ratio >=0 and ratio <= 1:
            self.__updateTurnSpeed(ratio)
            self.turnSpeedRatio = ratio
            if self.state in [self.fl, self.fr, self.bl, self.br]:
                self.state()

    def setRotSpeed (self, speed):
        if speed >=0 and speed < 128:
            self.rotSpeed = speed
            if self.state in [self.l, self.r]:
                self.state()
    

