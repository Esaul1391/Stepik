class Vector:
    def __init(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x > 0, self.y > 0

    def __int__(self):
        return int(self.x), int(self.y)

    def  __float__(self):
        return float(self.x), float(self.y)

    def __complex__(self):
        return complex(self.x), complex(self.y)