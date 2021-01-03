# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

direction_dict = {"STRAIGHT": "прямо", "LEFT": "налево", "RIGHT": "направо"}


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed} км/ч")

    def go(self):
        print(f"Автомобиль {self.name} начал своё движение.")

    def stop(self):
        print(f"Автомобиль {self.name} остановился.")

    def turn(self, direction):
        if direction_dict.get(str(direction).upper()):
            print(f"Автомобиль {self.name} движется {direction_dict.get(str(direction).upper())}.")
        else:
            print(f"Автомобиль {self.name} движется ВНИТУДА!!!")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превысили скорость на {self.speed - 60}км/ч")
        else:
            print(f"Скорость автомобиля {self.speed}км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превысили скорость на {self.speed - 40}км/ч")
        else:
            print(f"Скорость автомобиля {self.speed}км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


my_car = Car(150, "Red", "Lada 2101", False)
my_car.go()
my_car.show_speed()
my_car.turn("left")
my_car.turn("right")
my_car.turn("в пропасть")
my_car.stop()
print()

my_lamba = SportCar(250, "Yellow", "Lamborghini aventador")
my_lamba.go()
my_lamba.show_speed()
my_lamba.turn("left")
my_lamba.turn("right")
my_lamba.turn("к звездам")
my_lamba.stop()
print()

town_car = TownCar(84, "Black", "Fiat")
town_car.go()
town_car.show_speed()
town_car.turn("right")
town_car.turn("straight")
town_car.stop()
print(town_car.is_police)
print()

pol_car = PoliceCar(59, "Black-White", "Ford")
pol_car.go()
pol_car.show_speed()
print(pol_car.is_police)
pol_car.turn("left")
pol_car.turn("по кустам")
pol_car.turn("right")
pol_car.stop()
print()

work_car = WorkCar(71, "Orange", "Mini Cooper")
print(work_car.is_police)
work_car.go()
work_car.show_speed()
work_car.turn("straight")
work_car.turn("right")
work_car.stop()
print()

print(f"Имена всех созданных экземпляров: {work_car.name, town_car.name, pol_car.name, my_car.name, my_lamba.name}")