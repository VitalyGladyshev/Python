# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

import datetime

exit() # Не закочил :( Готов только каркас классов

class Toy:
    def __init__(self, name):
        self.name = name

class Bear(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name)
        self.toy_type = "Мишка"
        self.material = 20
        self.color = color

class Rabbit(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name)
        self.toy_type = "Зайчик"
        self.material = 18        
        self.color = color

class Pig(Toy):

    def __init__(self, name, color):
        Toy.__init__(self, name)
        self.toy_type = "Поросёнок"
        self.material = 15        
        self.color = color

class Order:
    __phase = 0
    __phase_dict = {0: "Создан", 1: "Заказ материалов", 2: "Пошив", 3: "Покраска", 4: "Упаковка", 5: "Хранение", 6: "Отгружен"}
    def __init__(self, name, color, toy_type):
        self.__phase_datetime_dict = {0: datetime.datetime.now(), 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 , 6: 0}
        if toy_type == "Bear":
            self.__toy_type = Bear(name, color)
        elif toy_type == "Rabbit":
            self.__toy_type = Rabbit(name, color)
        elif  toy_type == "Pig":
            self.__toy_type = Pig(name, color)
        else:
            self.__toy_type = False
    
    def next_phase(self):
        Order.__phase += 1
        self.__phase_datetime_dict[Order.__phase] = datetime.datetime.now()
        # действие: Заказ материалов, Пошив, Покраска, Упаковка, Хранение, Отгрузка

    def get_order_status(self):
        return "{} {}".format(self.__phase_dict[self.__phase], self.__phase_datetime_dict[self.__phase])

    def get_order_detail(self):
        return "{} {} {}".format(self.__toy_type.toy_type, self.__toy_type.name, self.__toy_type.color)

    
class Factory:
    toy_order_list = []

    def create_order(self, name, color, toy_type):
        new_order = Order(name, color, toy_type)
        Factory.toy_order_list.append(new_order)

    def get_production_status(self):
        for ind, order in  enumerate(Factory.toy_order_list):
            print(f"Заказ: {ind} Cтатус: {order.get_order_status()} Игрушка {order.get_order_detail()}")

    def set_production_status(self, index):
        if ind.isdigit():
            try:
                Factory.toy_order_list[int(ind) - 1].next_phase()
            except Exception:
                return False
        else:
            return False
        
fab_01 = Factory()
while(True):
    print("\n1. Создать новый заказ\n"
        "2. Вывести статус производства\n"
        "3. Завершение текущей операции по заказу\n"
        "4. Выход")
    choice = input("Выберите пункт: ")
    if choice == '1':
        print("\nТип игрушки:\n"
        "1. Мишка\n"
        "2. Зайчик\n"
        "3. Поросёнок\n")
        try:
            toy_type = int(input("Выберите тип: "))
        except Exception:
            print("Некорректный ввод!")
            continue
        toy_name = input("Введите название: ")
        toy_color = input("Введите цвет: ")
        fab_01.create_order(toy_name, toy_color, toy_type)
    elif choice == '2':
        fab_01.get_production_status()
    elif choice == '3':
        ind = input("Укажите индекс заказа по которому закончилась текущая операция: ")
        try:
            fab_01.set_production_status(int(ind))
        except Exception:
            print("Некорректный ввод!")
    elif choice == '4':
        break
    else:
        print("Некорректный ввод!")
