class ElectricCar:
    def __init__(self, color='black', owner=None):
        self.color = color
        self.owner = owner

car = ElectricCar(color='yellow', owner='Gvido')
car2 = ElectricCar(owner='Gvido')
car3 = ElectricCar()
car4 = ElectricCar('yellow', 'Gvido')
car5 = ElectricCar('yellow')
car6= ElectricCar(owner='Gvido', color='yellow')

print(car2.color, car2.owner)




# class ElectricCar:
#     def charge_battery(self):
#         print('Аккумулятор успешно заряжен')
#
#
# car = ElectricCar()
#
# ElectricCar.charge_battery(car)
# car.charge_battery()
# car.charge_battery(self)
# ElectricCar.charge_battery(self)
# ElectricCar.charge_battery(self, car)
# car.charge_battery(car)