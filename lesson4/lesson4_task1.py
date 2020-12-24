# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def get_salary(work_hours, reward_by_hour, prem):
    try:
        work_hours = int(work_hours)
        reward_by_hour = float(reward_by_hour)
        prem = float(prem)
    except TypeError:
        return print("Значения введены некорректно!")
    except ValueError:
        return print("Значения введены некорректно!")

    return (work_hours * reward_by_hour) + prem


script_name, work_hours, reward_by_hour, prem = argv

print(get_salary(work_hours, reward_by_hour, prem))
