# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    __products_quantity = {"Printers": 0, "Scanners": 0, "Xeroxes": 0}

    def __init__(self, capacity, location, country, phone):
        self.capacity = capacity
        self.location = location
        self.country = country
        self.phone = phone

    def add_product(self, count, *obj):
        try:
            if not count.isdigit():
                raise ValueError("Введено некорректное значение количества техники. Должно быть число.")

            count = int(count)
            for prod in obj:
                if isinstance(prod, Printer):
                    self.__products_quantity["Printers"] += int(count)
                if isinstance(prod, Scann):
                    self.__products_quantity["Scanners"] += int(count)
                if isinstance(prod, Xerox):
                    self.__products_quantity["Xeroxes"] += int(count)

            count_result = count * len(obj)
            print(f"Добавлено техники (ед.): {count_result}")
        except ValueError as err:
            print(err)

    def delete_product(self, count, *obj):
        try:
            if not count.isdigit():
                raise ValueError("Введено некорректное значение количества техники. Должно быть число.")

            count = int(count)
            for prod in obj:
                if isinstance(prod, Printer):
                    self.__products_quantity["Printers"] -= count
                if isinstance(prod, Scann):
                    self.__products_quantity["Scanners"] -= count
                if isinstance(prod, Xerox):
                    self.__products_quantity["Xeroxes"] -= count

            count_result = count * len(obj)
            print(f"Удалено техники (ед.): {count_result}")
        except ValueError as err:
            print(err)

    @property
    def get_products_quantity(self):
        return f"Отчет по количеству товара на складе: {self.__products_quantity}"


class OrgTech:
    def __init__(self, manufacturer, model, serial_number, price, paper_size):
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.paper_size = paper_size


class Printer(OrgTech):
    def __init__(self, manufacturer, model, serial_number, price, paper_size, type_of_printer):
        super(Printer, self).__init__(manufacturer, model, serial_number, price, paper_size)
        self.type_of_printer = type_of_printer


class Scann(OrgTech):
    def __init__(self, manufacturer, model, serial_number, price, paper_size, detector_material):
        super(Scann, self).__init__(manufacturer, model, serial_number, price, paper_size)
        self.detector_material = detector_material


class Xerox(OrgTech):
    def __init__(self, manufacturer, model, serial_number, price, paper_size, is_automatic_feeder):
        super(Xerox, self).__init__(manufacturer, model, serial_number, price, paper_size)
        self.is_automatic_feeder = is_automatic_feeder


my_wh = Warehouse(1, 2, 3, 4)
pr = Printer("HP", "2100hp", "453123h453kx43", 7000, "A4", "Laser")
sc = Scann("Canon", "d3500", "sssss345313dfgdfg", 5600, "A4", "diamond")
xr = Xerox("Xerox", "phaser 3020", "qqqwwwee1232werwe", 12000, "A3", True)

# Добавляем на склад по несколько раз одинаковые объекты. В реальной жизни такое невозможно. т.к. каждая единица
# имеет уникальный серийник и не может дублироваться. Но для ПЗ допустимо. При этом счетчики количества увеличиваются.
my_wh.add_product("1", pr, sc)
print(my_wh.get_products_quantity)

# Добавляем
my_wh.add_product("1", pr)
print(my_wh.get_products_quantity)
my_wh.add_product("2", sc, xr, sc)
print(my_wh.get_products_quantity)
my_wh.add_product("3", xr)
print(my_wh.get_products_quantity)

# Удаляем 2 единицы
my_wh.delete_product("два", xr)
print(my_wh.get_products_quantity)

# Удаляем по 2 единицы техники
my_wh.delete_product("2", pr, xr)
print(my_wh.get_products_quantity)
