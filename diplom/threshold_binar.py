import cv2 as cv


def nothing(x):
    pass


# Получаем изображение с камеры
cap = cv.VideoCapture(0)
# создаем окно
cv.namedWindow('result')
# создаем ползунки для минимальных и максимальных значений цветов
cv.createTrackbar('minB', 'result', 0, 255, nothing)
cv.createTrackbar('minG', 'result', 0, 255, nothing)
cv.createTrackbar('minR', 'result', 0, 255, nothing)
cv.createTrackbar('maxB', 'result', 0, 255, nothing)
cv.createTrackbar('maxG', 'result', 0, 255, nothing)
cv.createTrackbar('maxR', 'result', 0, 255, nothing)

signal = cv.imread('znak2.jpg')

while True:
    ret, frame = cap.read()
    # сохраняем текущее положение ползунка
    minB = cv.getTrackbarPos('minB', 'result')
    minG = cv.getTrackbarPos('minG', 'result')
    minR = cv.getTrackbarPos('minR', 'result')
    maxB = cv.getTrackbarPos('maxB', 'result')
    maxG = cv.getTrackbarPos('maxG', 'result')
    maxR = cv.getTrackbarPos('maxR', 'result')
    # бинаризованную картинку сохраняем в переменную и выводим на экран
    # mask = cv.inRange(frame, (minB, minG, minR), (maxB, maxG, maxR))
    # cv.imshow('mask', mask)
    mask2 = cv.inRange(signal, (minB, minG, minR), (maxB, maxG, maxR))
    cv.imshow('mask2', mask2)
    cv.imshow('signal', signal)
    # result = cv.bitwise_and(frame, frame, mask=mask)
    # cv.imshow('result', result)
    # result2 = cv.bitwise_and(signal, signal, mask=mask2)
    # cv.imshow('result2', result2)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
