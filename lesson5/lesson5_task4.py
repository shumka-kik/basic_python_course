# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

number_dict = {"Zero": "ноль", "One": "один", "Two": "два", "Three": "три", "Four": "четыре", "Five": "пять", "Six": "шесть", 
				"Seven": "семь", "Eight": "восемь", "Nine": "девять"}
try:
	with open("file_for_task4.txt", "r", encoding="UTF-8") as f:
		# Все новые строки которые будем вынимать из исходного файла и вставлять с заменой англ.чисел в новый файл.
		new_str_list = []

		while True:
			line = f.readline()
			if not line:
				break

			# Сплитим каждую строку и проверяем наличие в строке слова которое можем заменить значением из словаря.
			line_words = line.split(" ")
			for el in line_words:
				if el in number_dict:
					# Если искомое слово есть, то заменяем его и вставляем в общий список для нового файла.
					new_str_list.append(line.replace(el, number_dict[el]))

		new_file = open("new_file_for_task4.txt", "w")
		new_file.writelines(new_str_list)
		new_file.close()

		print("Программа успешно завершена!")
except Exception as e:
	raise e