import serial
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

# ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
# ser.flush()

cap = cv.VideoCapture('videoLine/allSignsLight.avi')
k = 0.11915  # 0.11915
while True:
    ret, frame = cap.read()
    frameCopy = frame.copy()  # копируем frame в переменную frameCopy
    cv.imshow("frame", frameCopy)
    fps = cv.waitKey(25)

    road = frameCopy[400:480, 130:510]  #
    road2 = road.copy()
    cmap = cv.cvtColor(road2, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(cmap, 50, 255, cv.THRESH_BINARY)
    cv.imshow("thresh1", thresh1)
    r = 0
    for i in thresh1[78]:
        if i < 50:  # поменял знак
            r += 1
    cnt = np.argmin(thresh1[78])  # поменял np.argmin на  np.argmax
    centr = cnt + r // 2

    cv.line(road2, (200, 200), (200, 100), (0, 250, 0), 2)
    cv.circle(road2, (centr, 75), 10, (0, 0, 255), -1)
    cv.imshow("warted", road2)
    cv.imshow("frame", frameCopy)

    d = centr - 190

    print(d)
    time.sleep(0.001)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
