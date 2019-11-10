# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    __direction = 0
    __speed = 0
    __engine_start = False

    def __init__(self, color, name='Car', speed_limit=90, is_police=False):
        self.__color = color
        self.__name = name
        self.__speed_limit = speed_limit
        self.__is_police = is_police

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        try:
            new_speed = int(new_speed)
        except Exception:
            return False
        if self.__engine_start:
            if new_speed <= self.__speed_limit:
                self.__speed = new_speed
            else:
                self.__speed = self.__speed_limit
            return self.get_speed()
        else:
            return False

    def stop(self):
        self.set_speed(0)
        self.__engine_start = False
        return self.get_speed()

    def go(self, speed = 10):
        self.__engine_start = True
        self.set_speed(speed)
        return self.get_speed()

    def turn(self, angle):
        self.__direction += angle
        return self.__direction


class TownCar(Car):
    def __init__(self, color):
        Car.__init__(self, color, "TownCar")


class SportCar(Car):
    def __init__(self, color):
        Car.__init__(self, color, "SportCar", 250)


class WorkCar(Car):
    def __init__(self):
        Car.__init__(self, "оранжевый", "WorkCar")


class PoliceCar(Car):
    def __init__(self):
        Car.__init__(self, "жёлтый", "PoliceCar", 250, True)


t_car_01 = TownCar("зелёный")
pol_csr_01 = PoliceCar()
print(f"{t_car_01.get_name()} цвет {t_car_01.get_color()} начинает движение: {t_car_01.go()} км/ч")
print(f"{t_car_01.get_name()} цвет {t_car_01.get_color()} увеличила скорость: {t_car_01.set_speed(85)} км/ч")
print(f"{pol_csr_01.get_name()} зафиксировано превышение ({t_car_01.get_speed()} км/ч) скоростного режима в городе автомобилем {t_car_01.get_name()} цвет {t_car_01.get_color()}")
print(f"{pol_csr_01.get_name()} цвет {pol_csr_01.get_color()} начинает движение: {pol_csr_01.go()} км/ч")
print(f"{t_car_01.get_name()} набирает максиальную скорость: {t_car_01.set_speed(200)} км/ч (сработало ограниечение)")
print(f"{pol_csr_01.get_name()} набирает скорость: {pol_csr_01.set_speed(180)} км/ч и догоняет {t_car_01.get_name()}")
print(f"{t_car_01.get_name()} цвет {t_car_01.get_color()} прекращает движение - скорость: {t_car_01.stop()} км/ч")
print(f"{pol_csr_01.get_name()} прекращает движение - скорость: {pol_csr_01.stop()} км/ч")
