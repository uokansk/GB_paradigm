import serial
#from picamera import PiCamera
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

ser = serial.Serial('/dev/ttyACM0',115200, timeout=1/100)
ser.flush()
cap = cv.VideoCapture(0)


nerovno = cv.inRange(cv.resize(cv.imread('Nerovno.jpg'), (64, 64)), (88, 133, 46), (255, 255, 255))
nPriori = cv.inRange(cv.resize(cv.imread('nPriori.jpg'), (64, 64)), (88, 133, 46), (255, 255, 255))
nPrior2 = cv.inRange(cv.resize(cv.imread('nPriori2.jpg'), (64, 64)), (88, 133, 46), (255, 255, 255))
parcking = cv.inRange(cv.resize(cv.imread('parcking2.jpg'), (64, 64)), (88, 70, 70), (255, 255, 255))
stop = cv.inRange(cv.resize(cv.imread('stop.jpg'), (64, 64)), (88, 133, 46), (255, 255, 255))

znak_number = 0
R = 0

k = 0.09

while True:
    ret, frame = cap.read()
    frameCopy = frame.copy()  # копируем frame в переменную frameCopy 
    cv.imshow("frameCopy", frameCopy)
    road = frameCopy[280:480, 120:520]
    road2 = road.copy()
    cv.imshow("road2", road2)
    cmap = cv.cvtColor(road, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold (cmap, 50, 255, cv.THRESH_BINARY)
    cv.imshow("thresh1", thresh1)
    r = 0
    for i in thresh1[190]:
        if i < 50:   #поменял знак
            r += 1
    cnt = np.argmin(thresh1[190])  #поменял np.argmin на  np.argmax 
    centr = cnt + r // 2

  #  cv.line(road2, (200, 200), (200,150), (0, 250, 0), 2)
    cv.circle(road2, (centr, 195), 10, (0, 0, 255), -1)
    cv.imshow("warted", road2)
   
    d = centr - 200
    y = d * k
    L = (52 + y)//1
#     ser.write(str(R).encode('utf-8'))
  
#     ser.write(b'%d \n' %R)
##################### определяем знаки  #########################
    znak = frameCopy[40 : 250, 400 : 635]
    cv.imshow('znak', znak) # закоментируй это для работы
#     frameCopy = frame.copy()
    znakGRAY = cv.cvtColor(znak, cv.COLOR_BGR2GRAY)
    
    Edge = cv.Canny (znakGRAY, 100, 255)
    cv.imshow('Edge', Edge)
    contours, hierarchy = cv.findContours(Edge, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    if contours == 0:        
        continue
    for cnt in contours:
        epsilon = 0.01*cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        area = math.fabs(cv.contourArea(cnt)) # вычисляем площадь контура
        
        if area < 5000 or area > 15000:
            continue
        x,y,w,h = cv.boundingRect(cnt) # получаем координаты верхнего угла, ширину и высоту
        sideRatio = w / h  #  получаем соотноение сторон
        if sideRatio < 0.4 or sideRatio > 1.2:
            continue        
        if sideRatio > 0.4 and sideRatio < 0.6:           
            cv.rectangle(znak,(x,y),(x+w,y+h),(0,255,0),2)
            detectZnak = cv.resize(znak[y : (y+h), x : (x+w)], (60, 120))
            #cv.imshow("detectZnak", detectZnak)   # чтобы видеть знак раскоментируй
                
            cutedFrame = detectZnak[20:101, 12:48]

            v = cv.cvtColor(cutedFrame, cv.COLOR_BGR2HSV)[:, :, 2]
            #cv.imshow("v", v)
                
            red_sum = np.sum(v[0:27, 0:36])
            yellow_sum = np.sum(v[28:54, 0:36])
            green_sum = np.sum(v[55:81, 0:36])
                
            cv.rectangle(cutedFrame, (0,0), (36,27),(0,0,255), 2)
            cv.rectangle(cutedFrame, (0,28), (36,54),(0,0,255), 2)
            cv.rectangle(cutedFrame, (0,55), (36,81),(0,0,255), 2)
#             cv.imshow("cutedFrame", cutedFrame)
                
            if green_sum > yellow_sum and green_sum > red_sum:
                R = 5
#                 print("green")
            elif yellow_sum > green_sum and yellow_sum > red_sum:
                R = 6
#                 print("yellow")
            elif red_sum > green_sum and red_sum > yellow_sum:
                R = 7
                print("red")
            else:
                print("red")
                R = 7
        else:
            cv.rectangle(znak,(x,y),(x+w,y+h),(0,255,0),2)
            detectZnak = znak[y : (y+h), x : (x+w)]
            #cv.imshow("detectZnak", detectZnak)
                
            detectZnak = cv.inRange(cv.resize(detectZnak, (64, 64)), (88, 100, 46), (255, 255, 255))
                
            stop_val = 0
            nerovno_val = 0
            nPriori_val = 0
            nPrior2_val = 0
           # priorit_val = 0
                
            for i in range (64):
                  for j in range (64):
                      if detectZnak[i][j] == stop[i][j]: stop_val +=1
                      if detectZnak[i][j] == nerovno[i][j]: nerovno_val +=1
                      if detectZnak[i][j] == nPriori[i][j]: nPriori_val +=1
                      if detectZnak[i][j] == nPrior2[i][j]: nPrior2_val +=1
                     # if detectZnak[i][j] == priorit[i][j]: priorit_val +=1
                
            if stop_val > 3000:
                R = 1
                    
            elif nerovno_val > 3000:
                R = 2
                   
            elif nPriori_val > 3000:
                R = 3
            
            elif nPrior2_val > 3000:
                R = 3
                    
           # elif priorit_val > 3000:
               # R = 4
                    
            else:
                R = 0

#         cv.imshow("znak", znak)
#     number = int.from_bytes(ser.read(), byteorder='big')
#     if number == 18:        
# #         ser.write(str(znak_number).encode('utf-8'))
#         ser.write(b'%d \n' %znak_number)
    ser.write(b'%d \n' %R)
    ser.write(b'%d \n' %L)
    print(R)
    print(L)
#     R = 0
    

#     print(R)
    if cv.waitKey(1)==ord('1'):
        break
cap.release()
cv.destroyAllWindows()



