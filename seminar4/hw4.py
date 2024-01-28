# Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
import math
from functools import reduce
from random import randint


def build_list(n, start_list, stop_list, a=None):
    if a is None:
        a = []
    for i in range(n):
        a.append(randint(start_list, stop_list))
    return a


def correlation(dat1, dat2):
    n = len(dat1)
    mean1 = sum(dat1)
    mean2 = sum(dat2)

    deviation1 = list(map(lambda x: x - mean1, dat1))
    deviation2 = list(map(lambda x: x - mean2, dat2))

    numerator = reduce(lambda x, y: x + y[0] * y[1], zip(deviation1, deviation2), 0)

    denominator = math.sqrt(reduce(lambda x, y: x + y ** 2, deviation1, 0)) * math.sqrt(
        reduce(lambda x, y: x + y ** 2, deviation2, 0))
    if denominator == 0:
        return 0
    return numerator / denominator


data2 = build_list(10, 1, 100)
data1 = build_list(10, 1, 10)

print(data1)
print(data2)
corr = correlation(data1, data2)
print(corr)
