#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.\

person_time = int(input("Мы с радостью переведем указанное вами количество секунд в привычный для человека формат чч:мм:сс.\nВведите время в секундах: "))
ostatok = person_time

hours = person_time // 3600
ostatok = person_time % 3600
minutes = ostatok // 60
seconds = ostatok % 60

print(f"Введенные вами {person_time} секунд отображаются как {hours:0>2}:{minutes:0>2}:{seconds:0>2}")