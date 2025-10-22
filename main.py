from typing import Callable, Any, Union


# Домашняя работа №7.1 — Практические задания
# Функции высшего порядка
# 1. Функция: map_every(elements, func, n)
def map_every(fun: Callable[[float], float], lst: list, ind: int) -> list:
    if ind < 0: raise ValueError("Неверное значение")
    new_lst = []
    for elm in lst[0::ind]:
        new_lst.append(fun(elm))
    return new_lst


print(map_every((lambda x: x * 10), [1, 2, 3, 4, 5, 6], 3))


# ***********************************************************************************************************
# 2. Функция: sum_by(numbers, func) и vector_length(x, y, z)
def sum_by(func, *arcs: float) -> float:
    return func(*arcs)


def vector_length(*arcs: float) -> float:
    result = round((sum_by(lambda x, y, z: x ** 2 + y ** 2 + z ** 2, *arcs)) ** 0.5, 2)

    return result


# ***********************************************************************************************************
# 3. Функция: take_while(elements, func)
def take_while(fun: Callable[[float], float], lst: list) -> list:
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


# Пример вызова:
fun_2 = lambda x: x / 2 > 2.1
print(take_while(fun_2, [1, 2, 3, 4, 5, 6]))


# ***********************************************************************************************************
# Задания на декораторы
# Задача 1 — count_calls (подсчёт вызовов)
def count_calls(fun: Callable[[str], None]) -> Callable:
    count = 0

    def wrapper(name: str):
        nonlocal count
        count += 1
        print(f'Функция {fun.__name__} вызвана {count}раз(а)')
        fun(name)

    return wrapper


@count_calls
def greet(name: str) -> None:
    print(f"Привет, {name}!\n")


# ***********************************************************************************************************
# Задача 2 — type_check(*types) (проверка типов аргументов)
def decorator_with_args(*d_args):
    def type_check(fun: Callable[[str], None]) -> Callable:
        def wrapper(*w_arcs: Any) -> Any:
            len_tuple = len(d_args)
            for i in range(len_tuple):
                assert isinstance(w_arcs[i], d_args[
                    i]), f'TypeError: Неверный тип аргумента N{i + 1}: ожидался {d_args[i]}, получен {type(w_arcs[i])}'
            result = fun(*w_arcs)
            return result

        return wrapper

    return type_check


@decorator_with_args(list, int, float, str)
def summ(a, b, c, d):
    print(''.join(a) + str(b) + str(c) + d)


# Пример вызова:
summ(['1', '2', '3', '4', '5'], 6, 7.3, 'python')


# Задача 3 — validate_range(min_value, max_value) (проверка диапазона)
def validate_range(value_min=0, value_max=100) -> Callable:
    def decorator(fun: Callable[[str], None]) -> Callable:
        def wrapper(*args) -> Union[int, float]:
            for elm in args:
                assert isinstance(elm,
                                  (int, float)), f"TypeError: ожидался тип <class 'int, float'>, получили {type(elm)}"
                assert elm >= value_min and elm <= value_max, f'ValueError: значение {elm} не соответствует диапазону {value_min}<=значение<={value_max}'
            result = fun(*args)
            return result

        return wrapper

    return decorator


@validate_range()
def set_percentage(value: Union[int, float]):
    print(f"Установлено значение: {value}%")


# Пример вызова:
set_percentage(-1)
