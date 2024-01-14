"""Условие
На вход подается: список целых чисел arr
Задача
Реализовать императивную функцию, которая возвращает три числа:
○ Долю позитивных чисел
○ Долю нулей
○ Долю отрицательных чисел"""


def weight_numbers(len_arr, count_p, count_n, count_z):
    return count_p / len_arr, count_n / len_arr, count_z / len_arr


def fractions_of_numbers(arr1, count_p=0, count_n=0, count_z=0):
    len_arr = len(arr1)
    for i in arr:
        if i < 0:
            count_n += 1
        elif i == 0:
            count_z += 1
        elif i > 0:
            count_p += 1
    return weight_numbers(len_arr, count_p, count_n, count_z)


def plus_minus(arr1):
    pos_cnt = len(list(filter(lambda x: x > 0, arr1)))
    neg_cnt = len(list(filter(lambda x: x < 0, arr1)))
    zer_cnt = len(list(filter(lambda x: x == 0, arr1)))
    counts = [pos_cnt, neg_cnt, zer_cnt]
    return list(map(lambda count: count / len(arr1), counts))


if __name__ == '__main__':
    arr = [0, 0, 1, 2, 0, 4, 5, -6, -7, 8, 9, -10]
    # arr = [1]
    solution = fractions_of_numbers(arr)
    solution2 = plus_minus(arr)

    print(solution)
    print()
    print(solution2)
