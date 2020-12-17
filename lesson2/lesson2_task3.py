# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

index_month = input("Введите индекс месяца от 1 до 12: ")

season_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
               7: "July", 8: "August", 9: "September", 10: "October", 11: "October", 12: "December"}

season_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "October", "December"]

# проверяем что введенный символ является положительным числом из диапазона от 1 до 12 включительно.
while not (index_month.isnumeric() and int(index_month) >= 1 and int(index_month) <= 12):
    index_month = input("Введенное значение не является числом из диапазона."
                        "\nВведите индекс месяца от 1 до 12: ")

# решение по словарю
print(season_dict.get(int(index_month)))
# решению по списку
print(season_list[int(index_month) - 1])