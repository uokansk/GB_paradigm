# Подключаем библиотеку
import cv2 as cv

# Видеозахват с камеры и присваеванм переменной cap
cap = cv.VideoCapture(0)
# В цикле считываем изображение в переменную frame и выводим картинку
while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    # выводим как выглядит переменная frame
    print(frame)
    # выводим тип переменной frame
    print(type(frame))
    # для корректной остановки программы используем условие по нажатию клавиши
    if cv.waitKey(1) == ord('q'):
        break
# останавливаем видео захват и закрываем все окна
cap.release()
cv.destroyAllWindows()
