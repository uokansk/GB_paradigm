"""для любого массива чисел array и любого числа target узнать содержится ли target в array."""
"""Реализовать императивную функцию поиска элементов на языке Python."""


def find_target_array(array, target):
    for i in array:
        if i == target:
            return True
        return False


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    solution = find_target_array(array, target)

    print(solution)
