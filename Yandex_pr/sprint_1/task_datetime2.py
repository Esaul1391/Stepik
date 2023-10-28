import datetime as dt

FORMAT = '%d.%m.%Y'


def get_days_to_birthda(name, date_birthday):
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT)
    date_birthday = date_birthday.date()
    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)

    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today_year + 1)

    days_left = date_birthday - today
    return f'{name}            {days_left}'


birthday = {
    ('lera', '16.05.2015'),
    ('max', '16.12.2011'),
    ('toly', '12.06.2016')
}

for dict in birthday:
    print(get_days_to_birthda(dict[0], dict[1]))
