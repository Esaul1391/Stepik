class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday

    def show_contact(self):
        print(f"{self.name}, {self.address}, {self.phone}, {self.birthday}")


leo = Contact('Лев Толстой',
              '+7 (123) 456-78-90',
              'Ясная Поляна',
              '9.09.1828')
mike = Contact('Михаил Булгаков',
               '2-03-27',
               'Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
               '15.05.1891')
vlad = Contact('Владимир Маяковский',
               '73-88',
               'Россия, Москва, Лубянский проезд, д. 3, кв. 12',
               '19.07.1893')


leo.show_contact()
