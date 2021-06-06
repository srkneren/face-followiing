import time
import serial

serx = serial.Serial("COM12",115200)
sery = serial.Serial("COM10",115200)
def dondur():
    derecex = int(input("x için 0 ile 180 arası"))

    serx.write(chr(derecex).encode())
    derecey = int(input("y için 0 ile 180 arası"))
    sery.write(chr(derecey).encode())
    time.sleep(0.1)
    
while 1:
    
    dondur()

