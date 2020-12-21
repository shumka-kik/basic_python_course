#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(param_1, param_2):
    try:
        print(param_1/param_2)
    except ZeroDivisionError:
        print("К сожалению, нельзя делить на ноль!")

while True:
    num_list = (input("Введите два числа через пробел: ")).split(" ")
    try:
        division(int(num_list[0]), int(num_list[1]))
        break
    except ValueError:
        print("Введенные значения не подходят под условие.")