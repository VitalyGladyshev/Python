# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import random

print("\nЗадание - 1\n")


def attack(person1, person2):
    person1["health"] -= person2["damage"] * random.randrange(90, 110, 10) / 100
    person2["health"] -= person1["damage"] * random.randrange(90, 120, 10) / 100
    return person1, person2


name_inp = input("В ведите имя игрока: ")
player = {"name": name_inp, "health": 100, "damage": 20}
name_inp = input("Введите имя противника: ")
enemy = {"name": name_inp, "health": 100, "damage": 20}

while player["health"] > 0 and enemy["health"] > 0:
    player, enemy = attack(player, enemy)
    print(f"{player['name']} сразился с {enemy['name']}! Здоровье {player['name']}: {player['health']}. "
        f"Здоровье {enemy['name']}: {enemy['health']}")
if player['health'] > 0:
    print(f"{player['name']} - победил! :)")
else:
    print(f"{player['name']} - проиграл! :(")

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print("\nЗадание - 2\n")


def damage(person):
    return person["damage"] * random.randrange(70 + person["luck"] * 10, 110 + person["luck"] * 10, 10) / 100


def attack(person1, person2):
    person1["health"] -= damage(person2) / person1["armor"]
    person2["health"] -= damage(person1) / person2["armor"]
    return person1, person2


name_inp = input("В ведите имя игрока: ")
player = {"name": name_inp, "health": 100, "damage": 20, "armor": 1, "luck": 3}
name_inp = input("Введите имя противника: ")
enemy = {"name": name_inp, "health": 100, "damage": 20, "armor": 1.3, "luck": 0}

while player["health"] > 0 and enemy["health"] > 0:
    player, enemy = attack(player, enemy)
    print(f"{player['name']} сразился с {enemy['name']}! Здоровье {player['name']}: {round(player['health'], 2)}. "
        f"Здоровье {enemy['name']}: {round(enemy['health'], 2)}")
if player['health'] > 0:
    print(f"{player['name']} - победил! :)")
else:
    print(f"{player['name']} - проиграл! :(")
