import cv2 as cv

signal = cv.imread('signals/znak2.jpg')
minBlue = 102
minGreen = 109
minRed = 134
maxBlue, maxGreen, maxRed = 255, 255, 255
cap = cv.VideoCapture(0)
while True:
    signal_copy = signal.copy()
    hsv = cv.cvtColor(signal, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv, (5, 5))

    mask = cv.inRange(hsv, (minBlue, minGreen, minRed), (maxBlue, maxGreen, maxRed))
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=4)
    cv.imshow('dilate', mask)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    if contours:
        contours = sorted(contours, key=cv.contourArea, reverse=True)
        cv.drawContours(signal_copy, contours, -1, (255, 0, 255), 2)
        cv.imshow('countours', signal_copy)

        (x, y, w, h) = cv.boundingRect(contours[0])
        cv.rectangle(signal_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow('rect', signal_copy)

    roiImg = signal[y:y + h, x:x + w]
    cv.imshow('detect', roiImg)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
