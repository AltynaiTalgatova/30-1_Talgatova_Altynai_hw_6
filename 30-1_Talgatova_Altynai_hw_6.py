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


def binary_search(searching_object, list1):
    list1.sort()

    middle = len(list1) // 2
    first = 0
    last = len(list1) - 1

    while list1[middle] != searching_object and first <= last:
        if searching_object > list1[middle]:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2

    if first > last:
        print('Not found')
    else:
        print(f'index = {middle}')


binary_search(88, [1, 5, 8, 12, 19, 25, 38, 49, 51, 64, 77, 88, 93, 100])
