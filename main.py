from typing import Callable

'''
# Домашняя работа №7.1 — Практические задания
# Функции высшего порядка
# 1. Функция: map_every(elements, func, n)

def map_every(fun: Callable[[float], float], lst: list, ind: int) -> list:
    assert ind > 0, 'ValueError, последний аргумент должен быть > 0'
    new_lst = []
    for elm in lst[0::ind]:
        new_lst.append(fun(elm))
    return new_lst


print(map_every(lambda x: x * 10, [1, 2, 3, 4, 5, 6], 2))


# 2. Функция: sum_by(numbers, func) и vector_length(x, y, z)
sum_by_fun = lambda x: x ** 2

def sum_by(fun: Callable[[float], float], *arcs: float) -> float:
    """
    Принимает fun функцию для вычисления длинны вектора в трёхмерном пространстве
    *arcs координаты векторов в 2D или 3D пространстве.
    :param fun: (x^2 + y^2 + z^2) ^ 0.5
    :param arcs: Координаты векторов 1, 2 или 1, 2, 3
    :return:
    """
    summ = 0
    for elm in arcs:
        summ += fun(elm)

    return summ


def vector_length(fun: Callable[[..., float], float]) -> Callable:
    def wrapper(*args: float):
        result = fun(*args)
        return result ** 0.5
    return wrapper


@vector_length
def sum_by(fun: Callable[[float], float], *arcs: float) -> float:
    """
    Принимает fun функцию для вычисления длинны вектора в трёхмерном пространстве
    *arcs координаты векторов в 2D или 3D пространстве.
    :param fun: (x^2 + y^2 + z^2) ^ 0.5
    :param arcs: Координаты векторов 1, 2 или 1, 2, 3
    :return:
    """
    summ = 0
    for elm in arcs:
        summ += fun(elm)

    return summ
'''

# 3. Функция: take_while(elements, func)
sum_by_fun = lambda x: x / 2 > 2.1
def take_while(fun: Callable[[float], float], lst:list) -> list:
    """
    Функция принимает произвольный список и возвращает новый в соответствии с критерием выбора
    :param fun: Произвольная функция критерия
    :param lst: Исходный список
    :return: Новый список соответствующий критерию
    """
    new_lst = []
    for elm in lst:
        if fun(elm):
            new_lst.append(elm)

    return new_lst