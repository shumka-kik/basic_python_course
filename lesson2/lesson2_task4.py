# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

input_str = input("Введите несколько слов, разделенных пробелами: ")
split_list = input_str.split(" ")

for ind, el in enumerate(split_list, 1):
    print(f"{ind} {el[0:10]}")