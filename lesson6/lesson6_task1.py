# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.


import time
import tkinter


color_list = ["Red", "Green", "Yellow"]
class TrafficLight:
    __color = "Yellow"
    # Счетчик для выхода из цикла работы светофора
    __counter = 6

    def running(self, color="yellow"):
        if color.title() in color_list:
            counter = 0
            self.__color = color
            while counter < self.__counter:
                counter += 1
                # Red
                if self.__color.title() == color_list[0]:
                    print(f"\033[30m\033[41m {self.__color.title()}")
                    time.sleep(7)
                    self.__color = color_list[2]
                # Green
                elif self.__color.title() == color_list[1]:
                    print(f"\033[30m\033[42m {self.__color.title()}")
                    time.sleep(10)
                    self.__color = color_list[0]
                # Yellow
                elif self.__color.title() == color_list[2]:
                    print(f"\033[30m\033[43m {self.__color.title()}")
                    time.sleep(2)
                    self.__color = color_list[1]
                else:
                    print("Косяк...")
            print(f"\033[0m Светофор завершил свою работу.")
        else:
            print("Светофор работает только в цветах: Red, Green, Yellow")


traf_light = TrafficLight()
traf_light.running("red")