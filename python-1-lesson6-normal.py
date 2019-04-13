# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

print("Задача - 1")

import os
import random


class Person:
    def __init__(self, name, health, damage, armor, luck):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__armor = armor
        self.__luck = luck

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health

    def set_health(self, health):
        try:
            health = float(health)
        except Exception:
            return False
        self.__health = health
        return True

    def get_damage(self):
        return self.__damage

    def get_armor(self):
        return self.__armor

    def get_luck(self):
        return self.__luck


class Game:
    def __init__(self, player1, player2):
        self.player01 = player1
        self.player02 = player2
        self.attack()

    def attack(self):
        while self.player01.get_health() > 0 and self.player02.get_health() > 0:
            self.player01.set_health(self.player01.get_health() - self.damage(player02) / self.player01.get_armor())   # person1["health"] -= damage(person2) / person1["armor"]
            self.player02.set_health(self.player02.get_health() - self.damage(player01) / self.player02.get_armor())   # person2["health"] -= damage(person1) / person2["armor"]
            print(f"{self.player01.get_name()} атаковал {self.player02.get_name()}! Здоровье {self.player01.get_name()}: {round(self.player01.get_health(), 2)}. "
                f"Здоровье {self.player02.get_name()}: {round(self.player02.get_health(), 2)}")
        if self.player01.get_health() > 0:
            print(f"{self.player01.get_name()} - победил! :)")
        else:
            print(f"{self.player01.get_name()} - проиграл! :(")    

    def damage(self, player):
        return player.get_damage() * random.randrange(70 + player.get_luck() * 10, 110 + player.get_luck() * 10, 10) / 100


name_inp = input("В ведите имя игрока: ")
player01 = Person(name_inp, 100, 20, 1, 3)   # player = {"name": name_inp, "health": 100, "damage": 20, "armor": 1, "luck": 3}

name_inp = input("Введите имя противника: ")
player02 = Person(name_inp, 100, 20, 1.3, 0)  # enemy = {"name": name_inp, "health": 100, "damage": 20, "armor": 1.3, "luck": 0}

Game(player01, player02)
