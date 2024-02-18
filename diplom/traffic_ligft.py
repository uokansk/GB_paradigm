import cv2 as cv
import numpy as np

heightLT = 210
widthLT = 70
i = 1
while True:
    # считываем картинку
    rgb_light = cv.resize(cv.imread('lightTraffic/' + str(i) + '.jpg'), (widthLT, heightLT))
    cv.imshow('light', rgb_light)

    # обрезаем фон
    cutTraffic = rgb_light[10:200, 12:58]
    cv.imshow('cut', cutTraffic)

    # переводим в формат HSV и выделяем самый яркий свет
    hsv = cv.cvtColor(cutTraffic, cv.COLOR_BGR2HSV)
    v = hsv[:, :, 2]
    cv.imshow('v', v)

    # складываем значения пикселей в каждой зоне
    redSum = np.sum(v[0:63, 0:46])
    yelSum = np.sum(v[64:127, 0:46])
    greSum = np.sum(v[128:190, 0:46])
    print('redSum', redSum, '  ', 'yelSum', yelSum, '  ', 'greSum', greSum)

    # увидеть выделенные области
    # cv.rectangle(cutTraffic, (0, 0), (46, 63), (0, 0, 255), 2)
    # cv.rectangle(cutTraffic, (0, 64), (46, 127), (0, 255, 255), 2)
    # cv.rectangle(cutTraffic, (0, 128), (46, 190), (0, 2500, 0), 2)
    # cv.imshow('region', cutTraffic)

    # сравниваем полученные суммы
    if greSum > yelSum and greSum > redSum:
        print('green')
    elif yelSum > greSum and yelSum > redSum:
        print('yellow')
    else:
        print('red')

    key = cv.waitKey(1)
    if key == ord('n'):
        i += 1
        cv.destroyAllWindows()

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
