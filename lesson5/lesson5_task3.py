# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из 
#сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


try:
	with open("file_for_task3.txt", "r", encoding="utf-8") as f:
		low_celery_workers = {}
		for line in f:
			line_values = line.split(" ")
			
			if float(line_values[1]) < 20000:
				print(line_values[0])
				low_celery_workers[line_values[0]] = line_values[1].replace("\n", "")

		summ = 0
		for val in low_celery_workers.values():
			summ += float(val)
		print(f"Среднее величина дохода сотрудников с окладом менее 20000 руб равна: {summ / len(low_celery_workers.keys()):.2f}")
except IOError as e:
	print("Вангую что-то с чтением/записью")
except ValueError:
	print("Вангую что-то со значениями")