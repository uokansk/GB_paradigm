import serial
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1 / 30)
ser.flush()
cap = cv.VideoCapture(0)

znak_number = 55
R = 7

k = 0.1

while True:
    ret, frame = cap.read()
    frameCopy = frame.copy()  # копируем frame в переменную frameCopy 
    cv.imshow("frameCopy", frameCopy)

    ser.write(str(R).encode('utf-8'))
    ser.write(b'%d \n' % R)
    ##################### определяем знаки  #########################

    number = int.from_bytes(ser.read(), byteorder='big')
    if number == 18:
        ser.write(str(znak_number).encode('utf-8'))
        ser.write(b'%d \n' % znak_number)
        ser.write(b'%d \n' % R)

    ser.write(str(znak_number).encode('utf-8'))
    print(znak_number)
    print(R)
    znak_number = 0
    time.sleep(0.01)

    print(R)
    if cv.waitKey(1) == ord('1'):
        break
cap.release()
cv.destroyAllWindows()
