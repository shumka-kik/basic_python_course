# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


# Начальный набор считаем что тоже был задан неотсортированным
input_list = [1, 4, 7, 5, 3, 2, 3, 2]

print(f"Исходный список: {input_list}")
input_list = sorted(input_list, reverse=True)

user_el = ""
while True:
    try:
        print(f"Отсортированный по убыванию список: {input_list}")
        user_el = input("Введите новый элемент списка или оставьте поле пустым для выхода из программы: ")

        # Условие выхода из программы
        if (user_el == ""):
            break

        user_el = int(user_el)

        # Проверяем новый элемент на вхождение в исходный список
        if (user_el in input_list):
            # Из-за того что список отсортирован по убыванию, то первое вхождение элемента (index) в отсортированном
            # по возрастанию списке даст нам индекс ПОСЛЕДНЕГО элемента (в отсортированном по убыванию списке)
            # одинаковых чисел после которого нужно вставить новый элемент.
            ind = (sorted(input_list).index(user_el))

            if ind == 0:
                # Если вставляемый элемент находится в самом конце списка
                input_list.append(user_el)
            else:
                input_list.insert(-ind, user_el)
        else:
            # Ветка для отсутствующих ранее элементов в списке.
            if int(user_el) > int(input_list[0]):
                # если новый элемент больше наибольшего элемента в списке (а он стоит в начале списка), то новый вставляем
                # в начало списка
                input_list.insert(0, user_el)
            elif int(user_el) < int(input_list[-1]):
                # если новый элемент меньше наименьшего элемента в списке (такой элемент находится в конце), то новый
                # элемент вставляем в конец списка с помощью append
                input_list.append(user_el)
            else:
                for i in range(len(input_list)):
                    # Ищем позицию для отсутствующего в списке элемента
                    if input_list[i] > user_el and input_list[i + 1] < user_el:
                        input_list.insert(i + 1, user_el)
    except ValueError:
        print("Неверно введено значение! Программа допускает только натуральные числа.")


