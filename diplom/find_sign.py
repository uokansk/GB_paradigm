import cv2 as cv

signal = cv.imread('signals/oncomingTraffic.png')
minBlue = 0
minGreen = 109
minRed = 114
minInRange = (minBlue, minGreen, minRed)
maxBlue, maxGreen, maxRed = 255, 255, 255
maxInRange = (maxBlue, maxGreen, maxRed)
pixel = 64
min_pixels = (pixel, pixel)

advantage = cv.inRange(cv.resize(cv.imread('reference_sign/myAdvantage.jpg'), min_pixels), minInRange, maxInRange)
no_advantage = cv.inRange(cv.resize(cv.imread('reference_sign/oncomingTraffic.jpg'), min_pixels), minInRange,
                          maxInRange)
slippery = cv.inRange(cv.resize(cv.imread('reference_sign/slipperyRoad.jpg'), min_pixels), minInRange, maxInRange)

while True:
    signal_copy = signal.copy()
    hsv = cv.cvtColor(signal, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv, (5, 5))

    mask = cv.inRange(hsv, (minBlue, minGreen, minRed), (maxBlue, maxGreen, maxRed))
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=4)
    cv.imshow('signal', mask)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    if contours:
        contours = sorted(contours, key=cv.contourArea, reverse=True)
        cv.drawContours(signal_copy, contours, -1, (255, 0, 255), 2)

        (x, y, w, h) = cv.boundingRect(contours[0])
        cv.rectangle(signal_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

        roiImg = signal[y:y + h, x:x + w]
        roiImg = cv.inRange(cv.resize(roiImg, min_pixels), minInRange, maxInRange)
        cv.imshow('detect', roiImg)

        advantage_val = 0
        no_advantage_val = 0
        slippery_val = 0
        for i in range(pixel):
            for j in range(pixel):
                if roiImg[i][j] == advantage[i][j]:
                    advantage_val += 1
                if roiImg[i][j] == no_advantage[i][j]:
                    no_advantage_val += 1
                if roiImg[i][j] == slippery[i][j]:
                    slippery_val += 1

        print(advantage_val, '   ', no_advantage_val, '   ', slippery_val)

        if advantage_val> 3000:
            print('advantage')
        elif no_advantage_val > 3000:
            print('no_advantage')
        elif slippery_val > 3000:
            print('slippery')
        else:
            print('nothing')

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
