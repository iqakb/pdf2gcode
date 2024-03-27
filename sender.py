import serial
import time
ser = serial.Serial("/dev/ttyUSB0", 115200)

# data = open('becus1.gcode', 'r').read()
# ser.write(str.encode("G0 X0 Y10\n"))

with open('becus1.gcode') as file:
    for line in file:
        print(line.rstrip())
        ser.write(str.encode(line.rstrip()+"\n"))
        