# -*- coding: utf-8 -*-
import cv2
import numpy as np


# TODO: Допишите импорт библиотек, которые собираетесь использовать


def load_tools():
    """ 
        Функция осуществляет загрузку модели(ей) нейросети(ей) из файла(ов).
        Выходные параметры: загруженный(е) модели(и)

        Если вы не собираетесь использовать эту функцию, пусть возвращает пустой список []
        Если вы используете несколько моделей, возвращайте их список [tool1, tool2]

        То, что вы вернёте из этой функции, будет передано вторым аргументом в функцию track_movement
    """

    # TODO: Отредактируйте функцию по своему усмотрению.
    # Модель нейронной сети, загрузите на онайн-платформу вместе с eval.py.

    # Пример загрузки моделей из файлов
    # Yolo-модели
    # net = cv2.dnn.readNetFromDarknet('yolo.cfg', 'yolo.weights')
    # yolo_model = cv2.dnn_DetectionModel(net)
    # yolo_model.setInputParams(scale=1/255, size=(416, 416), swapRB=True)
    # tools = [yolo_model]

    # Пример загрузки модели TensorFlow (не забудьте импортировать библиотеку tensorflow)
    # tf_model = tf.keras.models.load_model('model.h5')
    # tools.append(tf_model)

    tools = []
    return tools


def track_movement(video, tools) -> int:
    """
        Функция для трекинга автомобился.

        Входные данные: видео-объект (cv2.VideoCapture)
        Выходные данные: матрицу смежности графа в виде numpy массива (dtype=np.uint8)


        Примеры вывода:
            [[0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    """

    # TODO: Отредактируйте эту функцию по своему усмотрению.
    # Для удобства можно создать собственные функции в этом файле.
    # Алгоритм проверки один раз вызовет функцию load_tools
    # и для каждого тестового изображения будет вызывать функцию track_movement
    # Все остальные функции должны вызываться из вышеперечисленных.
    result = np.zeros((5, 5),
                      dtype=np.uint8)  # пустой список для засенения результата
    path = []
    while True:  # цикл чтения кадров из видео
        status, frame = video.read()  # читаем кадр
        if not status:  # выходим из цикла, если видео закончилось
            break
        frame = cv2.resize(frame, (872, 846))
        mask = cv2.inRange(frame, (2, 2, 2), (250, 250, 250))
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=3)
        first = np.sum(mask[43:153, 370:504])
        second = np.sum(mask[356:489, 34:140])
        third = np.sum(mask[350:496, 360:522])
        fourth = np.sum(mask[346:493, 731:850])
        fifth = np.sum(mask[690:805, 365:512])
        # print(first, second, third, fourth, fifth)
        if 2000 < first < 400000 and (len(path) == 0 or path[-1] != 0):
            if len(path) != 0:
                result[path[-1]][0] += 1
            path.append(0)
        elif 2000 < second < 400000 and (len(path) == 0 or path[-1] != 1):
            if len(path) != 0:
                result[path[-1]][1] += 1
            path.append(1)
        elif 2000 < third < 400000 and (len(path) == 0 or path[-1] != 2):
            if len(path) != 0:
                result[path[-1]][2] += 1
            path.append(2)
        elif 2000 < fourth < 400000 and (len(path) == 0 or path[-1] != 3):
            if len(path) != 0:
                result[path[-1]][3] += 1
            path.append(3)
        elif 7000 < fifth < 700000 and (len(path) == 0 or path[-1] != 4):
            if len(path) != 0:
                result[path[-1]][4] += 1
            path.append(4)
        # cv2.imshow('a', mask)
        # cv2.waitKey(100)
    print(path)
    return result
