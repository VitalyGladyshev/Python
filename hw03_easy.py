# Внимание!!! Домашнее задание ниже. (Задачи 2, 3..)
# Начал делать до начала урока. Не выбрасывать же...

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("\nЗадание-1_1\n")


def my_round(number, ndigits):
    source_str = str(number)
    dot_pos = source_str.find('.')
    if dot_pos < ndigits:
        destination_float = float(source_str[:ndigits + 1])
    else:
        destination_float = float(source_str[:ndigits])
    grad = dot_pos - ndigits
    if grad > 0:
        destination_float = destination_float * 10 ** grad
    if ndigits >= dot_pos:
        ndigits += 1
    if int(source_str[ndigits]) > 4:
        destination_float += 10 ** grad
    return destination_float


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# print(my_round(100454454545.454545, 5))
# for ind in range(1, 17):
#     print(my_round(123456789.123456789, ind))
for ind in range(1, 17):
    print(my_round(454545454.545454545, ind))
# for ind in range(1, 16):
#     print(my_round(545454545.454545454, ind))
print(f"float - это ЗЛО!!! При передаче в функцию ИСКАЖАЕТСЯ!!! Переделываем :(((")

print("\n\nЗадание-1_2\n")


def my_round_02(number, ndigits):
    source_str = str(number)
    dot_pos = source_str.find('.')
    if dot_pos < ndigits:
        destination_list = list(source_str[:ndigits + 1])
    else: 
        destination_list = list(source_str[:ndigits])
    if dot_pos <= ndigits:
        disp = ndigits + 1
    else:
        disp = ndigits
    if int(source_str[disp]) > 4:
        if int(destination_list[- 1]) + 1 > 9:
            destination_list[- 1] = '0'
            for ind in range(len(destination_list) - 2, 0, -1):    # обоаботка переносов
                if destination_list[ind] != '.':
                    if int(destination_list[ind]) + 1 > 9:
                        destination_list[ind] = '0'
                    else:
                        destination_list[ind]  = str(int(destination_list[ind]) + 1)
                        break
        else:
            destination_list[- 1] = str(int(destination_list[- 1]) + 1)        
    grad = dot_pos - ndigits
    if grad > 0:
        for _ in range(0, grad):
            destination_list.append('0')
    destination_str = ""
    for elem in destination_list:
        destination_str += elem
    return float(destination_str)

print(my_round_02(2.1234567, 5))
print(my_round_02(2.1999967, 5))
print(my_round_02(2.9999967, 5))

# print(my_round_02(100454454545.454545, 5))
# for ind in range(1, 17):
#     print(my_round_02(123456789.123456789, ind))
for ind in range(1, 16):
    print(my_round_02(454545454.545454545, ind))
# for ind in range(1, 15):
#     print(my_round_02(545454545.454545454, ind))


print("\n\nЗадание-1_3\n")  # модификация первого варианта (недопилена)


def my_round_03(number, ndigits):
    source_str = str(number)
    dot_pos = source_str.find('.')
    grad = dot_pos - ndigits
    ite = ndigits
    if ndigits >= dot_pos:
        ite = ndigits + 1
    if int(source_str[ite]) > 4:
        number += 10 ** grad
    source_str = str(number)    # нужна компенсация возможного сдвига позиции точки
    if dot_pos < ndigits:
        destination_float = float(source_str[:ndigits + 1])
    else:
        destination_float = float(source_str[:ndigits])
    if grad > 0:
        destination_float = destination_float * 10 ** grad
    return destination_float


print(my_round_03(2.1234567, 5))
print(my_round_03(2.1999967, 5))
print(my_round_03(2.9999967, 5))

# print(my_round_03(100454454545.454545, 5))
# for ind in range(1, 17):
#     print(my_round_03(123456789.123456789, ind))
# for ind in range(1, 17):
#     print(my_round_03(454545454.545454545, ind))
# for ind in range(1, 16):
#     print(my_round_03(545454545.454545454, ind))

# Задание-2:
