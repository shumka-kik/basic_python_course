#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_number = 0

while(number > 0):
    current_number = number % 10
    max_number = current_number if current_number > max_number else max_number
    number = number // 10

print(f"Максимальная цифра в введённом числе является: {max_number}")