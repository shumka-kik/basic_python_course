#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(user_text):
	input_list = user_text.split(" ")
	result_str = ""

	for word in input_list:
		char_list = list(word)
		is_bad_word = False

		for char in char_list:

			if ord(char) < 97 or ord(char) > 122:
				is_bad_word = True
				break

		if is_bad_word:
			result_str += " " + word
		else:
			result_str += " " + word.capitalize()
			

	result = f"Исходная строка: {user_text}\n Обработанная строка: {result_str}"

	return result

print(int_func(input("Введите слово/слова, разделенные пробелом, из маленьких латинских букв:")))