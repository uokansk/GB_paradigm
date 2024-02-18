import cv2 as cv
import os
import glob

i = 1
path = "C:/Users/kapa-/PycharmProjects/GB_paradigm/diplom"
sign = ['lightTraffic']
while True:
    key = cv.waitKey(1)
    if key == ord('n'):
        i += 1
        cv.destroyAllWindows()
    for clr in sign:
        path = os.path.join(path, clr)
        os.path.join(path, "*.jpg")
        filelist = (glob.glob(os.path.join(path, "*.jpg")))

        for filename in filelist:
            frame = cv.imread(filename)
            cv.imshow('light', frame)



    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
