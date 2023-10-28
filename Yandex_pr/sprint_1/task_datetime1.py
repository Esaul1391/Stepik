import datetime as dt


def get_days_to_birthda(date_birthday):
    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)

    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today_year+1)
        days_left = date_birthday - today
    else:
        days_left = date_birthday - today
    return days_left


viktor_birthday = dt.date(2015, 7, 9)
lev_birthday = dt.date(2021, 8, 5)

print(get_days_to_birthda(viktor_birthday))
print(get_days_to_birthda(lev_birthday))
