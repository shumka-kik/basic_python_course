# Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
	with open("file_for_task2.txt", "r") as f:
		count_lines = len(f.readlines())
		print(f"Всего в файле {count_lines} строк.")
		f.seek(0)
		counter = 1
		for line in f:
			count_word = len(line.split(" "))
			print(f"Строка {counter}: количество слов: {count_word}")
			counter += 1
except IOError as e:
	print("Что-то не так с записью/чтением")
except ValueError:
	print("Что-то не так с вводимым значением")

