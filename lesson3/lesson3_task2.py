#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birthday_year, city, email, phone):
    print(f"{name} {surname}, {birthday_year} года рождения из города {city}, контакты: E-mail: {email}, телефон: {phone}")

user_info(city="Таганрог", birthday_year="1990", name="Александр", surname="Чувашов", phone="366999", email="chuvashov@tracepharm.ru")

# Второй вариант с возвращаемым значением из функции
# def user_info(name, surname, birthday_year, city, email, phone):
#     return f"{name} {surname}, {birthday_year} года рождения из города {city}, контакты: E-mail: {email}, телефон: {phone}"
#
# print (user_info(city="Таганрог", birthday_year="1990", name="Александр", surname="Чувашов", phone="366999", email="chuvashov@tracepharm.ru"))