#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Введите сумму выручки фирмы: "))
costs = float(input("Введите издержки фирмы: "))

if((proceeds - costs) > 0 ):
    print(f"Фирма имеет прибыль: {(proceeds - costs):.2f}. "
          f"\nРентабельность выручки составляет: {((proceeds - costs)/proceeds):.2f}")
    person_count = int(input("Укажите количество сотрудников фирмы: "))
    profit_per_person = (proceeds - costs)/person_count
    print(f"Прибыль на одного сотрудника составляет: {profit_per_person:.2f}")
else:
    print(f"Фирма имеет убыток: {(costs - proceeds):.2f}")