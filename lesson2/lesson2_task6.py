# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
# программно, т.е. запрашивать все данные у пользователя.

my_list = []
list_params = ["Название", "Цена", "Количество", "Ед."]
ind = 1

while True:
    my_dict = {}
    # Заполняем первый кортеж значениями от пользака
    for i in range(4):
        my_dict[list_params[i]] = input(f"Введите {list_params[i]}: ")
    my_tuple = (ind, my_dict.copy())
    my_list.append(my_tuple)
    my_dict.clear()
    ind += 1

    add_elem = input("Ввести новый товар? Да/Нет: ")
    if add_elem.upper() != "ДА":
        break

analytical_dict = {}
params_list = [[], [], [], []]

# Пошла в ход мощнейшая аналитика. Собираем данные с имеющихся кортежей с товарами
for elem in my_list:
    params_list[0].append(elem[1].get("Название"))
    params_list[1].append(elem[1].get("Цена"))
    params_list[2].append(elem[1].get("Количество"))
    params_list[3].append(elem[1].get("Ед."))

for i in range(4):
    analytical_dict[list_params[i]] = params_list[i]

print(f"Аналитический вывод: {analytical_dict}")