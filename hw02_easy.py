# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Задание №1")

fruits_list = ["яблоко", "банан", "киви", "арбуз"]
for i in range(0, len(fruits_list)):
    print(f"{i + 1}. {fruits_list[i]:>7}")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("\nЗадание №2_01")

first_list = ["hi", "you", "we", 2, 34, 15, "we", 2, "we", 2]
second_list = ["yes", "no", "we", 2, 3, 65]

first_set = set(first_list)
second_set = set(second_list)
first_list = list(first_set - second_set)
print(f"{first_list}\n")

print("Задание №2_02")

first_list = ["hi", "you", "we", 2, 34, 15, "we", 2, "we", 2]
second_list = ["yes", "no", "we", 2, 3, 65]

for ind in second_list:
    while first_list.count(ind):
        first_list.remove(ind)
print(f"{first_list}\n")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задание №3")

source_list = [10, 20, 11, 21, 12, 22, 13, 23]
destination_list = []

for ind in source_list:
    if ind % 2:
        destination_list.append(ind * 2)
    else:
        destination_list.append(ind / 4)

print(destination_list)
