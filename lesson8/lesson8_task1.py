# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, text):
        self.date_text = text

    @classmethod
    def get_date_from_text(cls, text_of_date):
        dict_of_date_values = {}
        try:
            # взять строку
            find_list = str(text_of_date).split("-")
            dict_of_date_values["day"] = int(find_list[0])
            dict_of_date_values["month"] = int(find_list[1])
            dict_of_date_values["year"] = int(find_list[2])
        except ValueError:
            print("Введены некорректные значения, необходимо вводить цифры.")
            return ""
        else:
            # проверить числа на соответствие день, месяц, год методом check_date
            if cls.check_date(dict_of_date_values):
                return f"Введена корректная дата: {dict_of_date_values['day']:0>2}.{dict_of_date_values['month']:0>2}." \
                       f"{dict_of_date_values['year']}"
            else:
                return ""

    @staticmethod
    def check_date(date_dict):
        try:
            if date_dict["day"] < 1 or date_dict["day"] > 31:
                raise ValueError("Введенное значение Дня некорректно! День должен быть в числовом диапазоне между "
                                 "значениями 1 и 31.")
            if date_dict["month"] < 1 or date_dict["month"] > 12:
                raise ValueError("Введенное значение Месяца некорректно! Месяц должен быть в числовом диапазоне между "
                                 "значениями 1 и 12.")
            if date_dict["year"] < 1:
                raise ValueError("Введенное значение Года некорректно! Год должен быть положительным числом.")
        except ValueError as err:
            print(err)
            return False
        else:
            return True


my_class = Date("1-11-2020")
print(my_class.get_date_from_text(my_class.date_text)) # корректно

print(Date.get_date_from_text("12-12-1990"))   # корректно
print(Date.get_date_from_text("5-5-1990"))     # корректно
print(Date.get_date_from_text("ff-12-2000"))   # некорректно
print(Date.get_date_from_text("2-0-2000"))     # некорректно
print(f"Корректна ли дата? {Date.check_date({'day': 322, 'month': 4, 'year': 1861})}")  # некорректно
