import cv2 as cv


def nothing(x):
    pass


cap = cv.VideoCapture(0)
cv.namedWindow('result')
cv.createTrackbar('minB', 'result', 0, 255, nothing)
cv.createTrackbar('minG', 'result', 0, 255, nothing)
cv.createTrackbar('minR', 'result', 0, 255, nothing)
cv.createTrackbar('maxB', 'result', 0, 255, nothing)
cv.createTrackbar('maxG', 'result', 0, 255, nothing)
cv.createTrackbar('maxR', 'result', 0, 255, nothing)

signal = cv.imread('signals/slipperyRoad.jpg')


while True:

    # переводим формат изображения из BGR в HSV
    hsv = cv.cvtColor(signal, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)

    minB = cv.getTrackbarPos('minB', 'result')
    minG = cv.getTrackbarPos('minG', 'result')
    minR = cv.getTrackbarPos('minR', 'result')
    maxB = cv.getTrackbarPos('maxB', 'result')
    maxG = cv.getTrackbarPos('maxG', 'result')
    maxR = cv.getTrackbarPos('maxR', 'result')
    # применяем размытие
    hsv = cv.blur(hsv, (5, 5))
    cv.imshow('blur', hsv)

    # бинаризованную картинку сохраняем в переменную и выводим на экран
    mask = cv.inRange(hsv, (minB, minG, minR), (maxB, maxG, maxR))
    cv.imshow('mask', mask)

    maskEr = cv.erode(mask, (5, 5), iterations=2)
    cv.imshow('erode', maskEr)

    maskDi = cv.dilate(maskEr, None, iterations=2)
    cv.imshow('dilate', maskDi)

    result = cv.bitwise_and(signal, signal, mask=mask)
    cv.imshow('result', result)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
