# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
import re

class ComplexNumber:
    def __init__(self, complex_number):
        # ищем сначала значение с мнимой i
        second_value = re.search(r"[+-]?\d*[i]{1}", complex_number)
        # затем отсекаем её из строки и получаем первое вещественное число
        first_value = str(complex_number).split(second_value[0])

        # нам нужно только число со знаком +/- для выполнения расчетов, а мнимое i добавим при выводе на экран
        self.second_value = second_value[0].replace("i", "")
        self.first_value = first_value[0]

    def __str__(self):
        return f"{self.first_value}{self.second_value if self.second_value != 1 else ''}i"

    def __add__(self, other):
        first_value = int(self.first_value) + int(other.first_value)
        second_value = int(self.second_value) + int(other.second_value)

        # Если нет мнимой части i значит число уже не комплексное, а обычное
        if second_value == 0:
            return f"{first_value}"
        return ComplexNumber(f"{first_value}{second_value}i" if second_value < 0 else f"{first_value}+{second_value}i")

    def __mul__(self, other):
        first_value = int(self.first_value) * int(other.first_value) \
                      + int(self.second_value) * int(other.second_value) * -1
        second_value = int(self.first_value) * int(other.second_value) + int(self.second_value) * int(other.first_value)

        # Если нет мнимой части i значит число уже не комплексное, а обычное
        if second_value == 0:
            return f"{first_value}"
        return ComplexNumber(f"{first_value}{second_value}i" if second_value < 0 else f"{first_value}+{second_value}i")


my_cn1 = ComplexNumber("3+2i")
my_cn2 = ComplexNumber("5-2i")

# Результат совпадает с представленным решением на странице
# https://xn--24-6kcaa2awqnc8dd.xn--p1ai/kompleksnye-chisla.html
print(f"Результат сложения: {my_cn1 + my_cn2}")
print(f"Результат умножения: {my_cn1 * my_cn2}")