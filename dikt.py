import datetime as dt

def get_days_to_birthday(data_br):
    today = dt.date.today()
    today_year = today.year
    data_br_year = data_br.replace(year=today_year)

    if data_br_year < today:
        data_br_year = data_br.replace(year=today_year + 1)

    return abs((data_br_year - today).days)

lera_br = dt.date(2015, 5, 16)
max_br = dt.date(2011, 12, 16)



print("До дня рождения Леры осталось", get_days_to_birthday(lera_br), "дней")
print("До дня рождения Максима осталось", get_days_to_birthday(max_br), "дней")
