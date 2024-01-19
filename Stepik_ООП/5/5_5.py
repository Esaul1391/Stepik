class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, n):
        return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)

    def __truediv__(self, n):
        return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)

    def __floordiv__(self, n):
        return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)


