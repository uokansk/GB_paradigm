"""для любого массива чисел array и любого числа target узнать содержится ли target в array."""
"""Реализовать императивную функцию поиска элементов на языке Python."""


def find_target_array(arr, tar):
    for i in arr:
        if i == tar:
            return True
    return False


def search_declarative(arr, tar):
    return tar in arr


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 3

    solution_imper = find_target_array(array, target)
    solution_dec = search_declarative(array, target)

    print()
    print("solution_imper = ", solution_imper)
    print("solution_dec = ", solution_dec)
