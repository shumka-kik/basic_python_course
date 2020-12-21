#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(param_1, param_2, param_3):
    my_list = [param_1, param_2, param_3]
    my_list.remove(min(my_list))
    result = sum(my_list)
    return result

print(my_func(6, 5, 10))