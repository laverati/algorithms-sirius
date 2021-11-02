# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и
# вернуть его индекс. Если x в массиве не встречается - вернуть -1.
 
# Решить задачу применяя алгоритм бинарного поиска

def linear_search(numbers, x):
    for index in range(len(numbers)):
        if numbers[index] == x:
            return index # если нашли - возвращаем индекс

    return -1 # если не нашли - возвращаем -1


def binary_search(numbers, x):
    sorted(numbers)
    left = -1
    right = len(numbers) 

    while right > left + 1:
        middle = (left + right) // 2

        if numbers[middle] >= x:
           right = middle
        else:
            left = middle
    return right


def test(result, awaiting_result):
    if result == awaiting_result:
        print("Ok")
    else:
        print("Ошибка", result, "!=", awaiting_result)
 
test(linear_search([5, 2, 8, 15, 11], 1), -1)
test(linear_search([5, 2, 8, 15, 11], 8), 2)
test(linear_search([5, 2, 8, 15, 11], 15), 3)
test(linear_search([5, 2, 8, 15, 11], 5), 0)


test(binary_search([5, 2, 8, 15, 11], 2), 0)
test(binary_search([5, 2, 8, 15, 11], 15), 3)
test(binary_search([5, 2, 8, 15, 11], 5), 4)
test(binary_search([5, 2, 8, 15, 11], 1), -1)