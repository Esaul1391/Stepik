import datetime as pt

FORMAT = ('%H:%M:%S')

weight = 100

height = 190

k_1 = 0.035
k_2 = 0.029

step_m = 70

transfer_cof = 1000

storage_data = {}

def check_correct_data(data):
    if len(data) !=2 or data[0] is None or data[1] is None:
        return False
    return True

def chek_correct_time(time):
    if storage_data is not None:
        for item in storage_data:
            if pt.datetime.strptime(item, FORMAT).time() >= time:
                return False
        else:
            return True

def get_step_day(steps):
    for step in storage_data.values():
        steps += step
    return steps

def get_distance(steps):
    distant = round(steps * step_m/transfer_cof, 2)
    return distant

def get_spent_calories(dist, current_time):
    hours = current_time.hour + current_time.minute/60
    mean_spead = dist / (hours)
    spent_colories = round((k_1 * weight +(mean_spead**2/height)*k_2*weight)*hours*60,2)
    return spent_colories

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


def show_message(time, steps, dist, calories, achievement):
    print(f'''
        Время: {time}.
        Количество шагов за сегодня: {steps}.
        Дистанция составила {dist:.2f} км.
        Вы сожгли {calories:.2f} ккал.
        {achievement}
        ''')


def accept_package(data):
    """Обработать пакет данных."""
    if check_correct_data(data) is False:
        return 'Некорректный пакет'
    time, steps = data
    pack_time = pt.datetime.strptime(time, FORMAT).time()
    if chek_correct_time(pack_time) is False:
        return 'Некорректное значение времени'
    day_steps = get_step_day(steps)
    dist = get_distance(steps) + get_distance(sum(storage_data.values()))
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data.update({data})
    return storage_data


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
