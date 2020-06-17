import serial



class BodyHeatMeasure:

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)


    def measureHeat(self):
        heatData = str(self.ser.readline(), 'utf-8')[0:5]
        return heatData




if __name__ == "__main__":
    bodyHeat = BodyHeatMeasure()

    while True:
        print(bodyHeat.measureHeat())