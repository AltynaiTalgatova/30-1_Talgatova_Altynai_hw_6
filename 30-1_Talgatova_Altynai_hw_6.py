# ДЗУрок6 ДЭДЛАЙН 25.05.2023 23 59
# ДЗ*:
# 1. Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего параметра
# не отсортированный список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию
# 4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и
# список в котором необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    print(f'Sorted List: {unsorted_list}')


bubble_sort([88, 58, 7, 11, 12, 39, 23, 77])


def binary_search1(val, n):
    n = 5000
    result_ok = False
    first = 0
    last = n - 1
    while first < last:
        middle = (first + last) // 2
        if val == middle:
            first = middle
            last = first
            result_ok = True
        elif val > middle:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'index: {first}')
    else:
        print('this number does not exist')


binary_search1(88, [1, 5, 8, 12, 19, 25, 38, 49, 51, 64, 77, 88, 93, 100])