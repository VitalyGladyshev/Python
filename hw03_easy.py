# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("Задание-1_1\n")


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

print(my_round(100454454545.454545, 5))
for ind in range(1, 17):
    print(my_round(454545454.545454545, ind))
for ind in range(1, 16):
    print(my_round(545454545.454545454, ind))
print(f"float - это ЗЛО!!! При передаче в функцию ИСКАЖАЕТСЯ!!! Переделываем :(((")

print("\nЗадание-1_2\n")


def my_round_02(number, ndigits):
    destination_list = list(str(number)) 
    
    # source_str = str(number)
    # dot_pos = source_str.find('.')
    # destination_str = ""
    # if dot_pos < ndigits:
    #     destination_str += source_str[:ndigits + 1]
    # else:
    #     destination_str += source_str[:ndigits]

    
    # for cnt in reversed(destination_list):
        

    # grad = dot_pos - ndigits
    # if grad > 0:
    #     destination_float = destination_float * 10 ** grad
    # if ndigits >= dot_pos:
    #     ndigits += 1
    # if int(source_str[ndigits]) > 4:
    #     destination_float += 10 ** grad

    return destination_list


print(my_round_02(2.1234567, 5))
print(my_round_02(2.1999967, 5))
print(my_round_02(2.9999967, 5))

print(my_round_02(100454454545.454545, 5))
for ind in range(1, 17):
    print(my_round_02(454545454.545454545, ind))
for ind in range(1, 16):
    print(my_round_02(545454545.454545454, ind))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("\nЗадание-2\n")

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
