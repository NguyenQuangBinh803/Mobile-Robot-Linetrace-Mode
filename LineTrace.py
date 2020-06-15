import sys
import threading
import time
import serial
from UtilitiesMacroAndConstant import *

class Linetrace:
    def __init__(self, port, baud_rate):
        self.value = 0
        try:
            print("Opening serial port: %s..." % port + ".")
            self.robot_serial = serial.Serial(port, baud_rate, timeout=0.05)
            time.sleep(1)
            self.robot_serial.reset_input_buffer()
            threading.Thread(target=self.flush_data_serial).start()
        except serial.serialutil.SerialException:
            print("Serial not found at port " + port + ".")
            sys.exit(0)

    def flush_data_serial(self):
        self.robot_serial.read(self.robot_serial.in_waiting)
        time.sleep(0.3)

    def map(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin) / float(leftSpan)
        return rightMin + (valueScaled * rightSpan)

    def read_data_sensor(self):
        raw_data = self.robot_serial.read_all().decode("utf-8")
        data = raw_data.splitlines()
        if data != [] and data[-1][-1] == ';':
            self.value = int(data[-1][:-1])

    def angle_from_sensor(self):
        self.read_data_sensor()
        max = 0
        count = 0
        curve = False
        prev_i = -1
        for i in range(8):
            if self.value & (1 << i) == (1 << i):
                if prev_i == -1:
                    prev_i = i
                elif i - prev_i > 2:
                    curve = True
                    prev_i = i
                max += i
                count += 1
        if count != 0:
            new_value = self.map(max / count, 0, 8, 4, -4)
            return (curve, math.atan(((new_value * DISTANCE_BETWWEN_LED - DISTANCE_BETWWEN_LED / 2) / MR_DISTANCE_FROM_CENTER_TO_SENSOR)) * 180 / math.pi)

if __name__ == "__main__":
    linetrace = Linetrace(PORT, BAUDRATE)
    while (1):
        print(linetrace.angle_from_sensor())
        time.sleep(0.2)
