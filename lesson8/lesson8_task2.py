# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class ZeroException(Exception):
    def __init__(self, text):
        self.text = text


try:
    number1 = int(input("Введите делимое: "))
    number2 = int(input("Введите делитель: "))

    if number2 == 0:
        raise ZeroException("На ноль делитель нельзя!")
    result = number1 / number2
except ValueError:
    print("Вы ввели не число")
except ZeroException as err:
    print(err)
else:
    print(f"Все хорошо. Результат: {result}")
