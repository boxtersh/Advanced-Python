# Домашняя работа №7.1 — Практические задания
# Функции высшего порядка
# 1. Функция: map_every(elements, func, n)

def map_every(fun, lst: list, ind):
    assert ind >= 0, 'ValueError, последний аргумент должен быть >= 0'
    new_lst = []
    for elm in lst[0::ind]:
        new_lst.append(fun(elm))
    return new_lst


print(map_every(lambda x: x * 10, [1, 2, 3, 4, 5, 6], 3))
