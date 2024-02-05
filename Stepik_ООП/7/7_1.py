class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = 0
    def inc(self, num=None):
        if isinstance(num, int):
            self.value += num

        if isinstance(num, None):
            self.value += 1


    def dec(self, num):
        if isinstance(num, int):
            if (self.value + num) < 0:
                self.value = 0
            else:
                self.value += num

        if isinstance(num, None):
            if (self.value - 1) < 0:
                self.value = 0
            else:
                self.value -= 1




# class Validator:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def is_valid(self):
#         return None
#
#
# class NumberValidator(Validator):
#     def is_valid(self):
#         if isinstance(self.obj, (int, float)):
#             return True
#         return False

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def skip_ads(self):
#         return False
#
# class PremiumUser(User):
#     def skip_ads(self):
#         return True


# class Animal:
#     def sleep(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Fish(Animal):
#     def swim(self):
#         pass
#
#
# class Bird(Animal):
#     def lay_eggs(self):
#         pass
#
#
# class FlyingBird(Bird):
#     def fly(self):
#         pass

# class Shape:
#     pass
#
#
# class Polygon(Shape):
#     pass
#
#
# class Circle(Shape):
#     pass
#
#
# class Quadrilateral(Polygon):
#     pass
#
#
# class Triangle(Polygon):
#     pass
#
# #
# # class Parallelogram(Quadrilateral):
# #     pass
#
#
# class Rectangle(Parallelogram):
#     pass
#
#
# class Square(Rectangle):
#     pass
#
#
# class IsoscelesTriangle(Triangle):
#     pass
#
#
# class EquilateralTriangle(Triangle):
#     pass

# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class WaterVehicle(Vehicle):
#     pass
#
#
# class AirVehicle(Vehicle):
#     pass
#
#
# class Car(LandVehicle):
#     pass
#
#
# class Motorcycle(LandVehicle):
#     pass
#
#
# class Bicycle(LandVehicle):
#     pass
#
#
# class Propeller(AirVehicle):
#     pass
#
#
# class Jet(AirVehicle):
#     pass
