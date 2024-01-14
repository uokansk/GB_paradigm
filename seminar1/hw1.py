# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


from random import randint


def build_list(n, start_list, stop_list, a=None):
    if a is None:
        a = []
    for i in range(n):
        a.append(randint(start_list, stop_list))
    return sort_list_imperative(a), sort_list_declarative(a)


def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    amount_numbers = 10
    beginning_list = -99
    end_list = 99
    solution = build_list(amount_numbers, beginning_list, end_list)
    print(solution)
