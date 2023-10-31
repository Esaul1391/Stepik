import math


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius ** 2
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = self.average_temp_celcius * 9 / 5 + 32

    def show_info(self):
        print(f'Planet {self.name} has square surface {self.surface_area}')
        print(f'average temp. surface planet: {self.average_temp_fahrenheit} fahrenheit')


jupiter = Planet("Jupiter", 69911, -108)
jupiter.show_info()
