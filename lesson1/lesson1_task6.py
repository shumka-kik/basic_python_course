#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


current_distance = int(input("Добрый день!"
                             "\nМы предлагаем вам рассчитать количество дней за которое вы сможете набрать необходимую дистанцию для пробежки."
                             "\nВведите текущую преодолеваемую дистанцию: "))
desired_distance = int(input("Введите желаемую дистанцию для пробежки: "))

count = 1
print(f"{count}-й день: {round(current_distance, 2)}")

while(current_distance < desired_distance):
    current_distance = current_distance * 1.1
    count += 1
    print(f"{count}-й день: {round(current_distance, 2)}")


print(f"Вам необходимо {count} дня/дней для того, чтобы выйти на желаемую дистанцию пробежки в {desired_distance} км.")