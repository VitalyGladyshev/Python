# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

dig = 100
while not 0 < dig < 10:
    dig = int(input("Введите целое число больше 0, но меньше 10: "))
print(dig, "** 2 = ", dig ** 2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

var1 = int(input("Введите целое число 1: "))
var2 = int(input("Введите целое число 2: "))
var1 += var2
var2 = var1 - var2
var1 -= var2
print("Числа взаимно заменены: Первое = ", var1, " Второе = ", var2)
