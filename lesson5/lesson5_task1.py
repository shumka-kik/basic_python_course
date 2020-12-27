# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.


try:
	with open("lesson5_task1_f.txt", "w") as f:
		while True:
			insert_line = input("Введите строку или оставьте её пустой для выхода из программы: ")
			if insert_line == "":
				print("Программа завершена!")
				break
			f.writelines([insert_line, "\n"])
except IOError as e:
	print(f"Что то не так с чтением/записью: {e}")
except ValueError:
	print("Что то не так с вводимыми значениями")