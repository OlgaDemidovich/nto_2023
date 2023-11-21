# -*- coding: utf-8 -*-
import socket
# TODO: Допишите импорт библиотек, которые собираетесь использовать


def setup_socket(ip_address, port):
    """ Функция инициализирует сокет.
        Входные параметры: ip-адрес и порт сервера
        Выходные параметры: инициализированный сокет

        Если вы не собираетесь использовать эту функцию, пусть возвращает None

        То, что вы вернёте из этой функции, будет передано первым аргументом в функцию communication_cycle
    """
    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.connect((ip_address, port))
    # return server
    return None


def communication_cycle(conn: socket.socket, start_pos, start_equipment):
    """ Эта функция отвечает за обмен данными с информационным и сервисным центрами..
        Входные параметры: 
            conn - сокет из функции setup_socket, 
            start_pos - стартовая позиция беспилотного автомобиля (x, y),
            start_equipment - начальное снаряжение

    """
    conn.send('hello! World'.encode())
    answer = conn.recv(1024).decode()
    conn.close()
