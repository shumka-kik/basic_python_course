# Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.


class Worker:
    _income = {}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


my_pos = Position("Киса", "Воробьянинов", "Гигант мысли", {"wage": 36700, "bonus": 1200})
my_pos.get_full_name()
my_pos.get_total_income()

poser = Position("Остап", "Бендер", "Великий комбинатор", {"wage": 100000, "bonus": 25000})
poser.get_full_name()
poser.get_total_income()
