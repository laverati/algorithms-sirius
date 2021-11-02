# Дан массив целых чисел numbers и целое число x;
# нужно найти в массиве два элемента, сумма которых равняется x.

# Гарантируется, что в такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предложить второе решение, которое оптимизирует наивный алгоритм
# cприменением сортировки или вспомогательных структур

numbers = [1, 2, 4, 1, 7, 89, 45, 21, 58, 90, 653, 5, 6]
x = 11
# первый метод: наивный
print("Первый способ:")
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[i] + numbers[j] == x:
            print("Нужные элементы: ", numbers[i], numbers[j])
            break

#Второй метод, оптимизированный:
print("Второй способ:")

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

quick_sort(numbers)
for i in range(len(numbers) - 1):
    if numbers[i] < x:
        for j in range(len(numbers) - i - 1):
            if numbers[i] + numbers[j] == x:
                print("Нужные элементы: ", numbers[i], numbers[j])
    else:
        break