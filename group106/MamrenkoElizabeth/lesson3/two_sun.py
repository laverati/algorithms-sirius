# Дан массив целых чисел numbers и целое число x;
# нужно найти в массиве два элемента, сумма которых равняется x.
 
# Гарантируется, что в такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предложить второе решение, которое оптимизирует наивный алгоритм
# cприменением сортировки или вспомогательных структур

numbers = [1, 2, 4, 1, 7, 89, 45, 21, 58, 90, 653, 5, 6]
x = 11
#первый метод: наивный
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[i]+ numbers[j] == x:
            print("Нужные элементы: ", numbers[i], numbers[j])


 # numbers = list(map(int, input().split()))
 # sum = int(input())

 # print('primary', 'two_sum_ptimary(numbers, sum))
 # print('optimized', 'two_sum_primary(numbers, sum))

