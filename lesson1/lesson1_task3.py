#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Н
# апример, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число: ")

print(f"{number} + {number*2} + {number*3} = + {int(number) + int(number*2) + int(number*3)}")