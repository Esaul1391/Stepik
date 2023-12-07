from datetime import date

def date_formatter(country_code):
    d = {'ru': '%d.%m.%Y',
         'us': '%m-%d-%Y',
         'ca': '%Y-%m-%d',
         'br': '%d/%m/%Y',
         'fr': '%d.%m.%Y',
         'pt': '%d-%m-%Y', }
    def format_date(date):
        return date.strftime(d[country_code])
    return format_date

date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))

# import math
# def power(degree):
#     def deg(x):
#         return pow(x, degree)
#     return deg
# square = power(2)
# print(square(5))