# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


def rand_list_gen(list_len, bn_a = 0, bn_b = 10):
    rand_list = [random.randint(bn_a, bn_b) for _ in range(list_len)]
    return rand_list 


print("Задание-1")

source_list = rand_list_gen(12)
print(f"Список источник: {source_list}")

destination_list = [source_list[ind] ** 2 for ind in range(len(source_list))]
print(f"Список квадратов: {destination_list}")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print("Задание-2")

first_fruits_list = ["яблоко", "банан", "апельсин", "манго"]
print(first_fruits_list)
second_fruits_list = ["ананас", "абрикос", "яблоко", "виноград", "банан"]
print(second_fruits_list)

destination_list = [ind_1 for ind_1 in first_fruits_list for ind_2 in second_fruits_list if ind_1 == ind_2]
print(f"Пересечение списков: {destination_list}")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print("Задание-3")

source_list = rand_list_gen(30, -10, 100)
print(f"Список источник: {source_list}")

destination_list = [ind for ind in source_list if ind > 0 and not ind % 3 and ind % 4]
print(f"Элементы кратны 3, положительны, не кратны 4: {destination_list}")
