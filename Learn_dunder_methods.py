from math import *
#Создай класс Vector, который поддерживает сложение (+) и вычитание (-) векторов.
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __mul__(self, scalar):# * 
       return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar): # /
        if scalar == 0:
            raise ZeroDivisionError
        return Vector(self.x / scalar, self.y / scalar)
    
    def __len__(self):
        return round(sqrt((self.x ** 2) + (self.y ** 2)))
    
    def __iter__(self):
        return iter([self.x, self.y])

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    def __bool__(self):
        if self.x == 0 and self.y == 0:
            return False
        return True

    def __rmul__(self, scalar):
        return self * scalar
    
    def __radd__(self, scalar):
        return self + Vector(scalar, scalar)

    def __rsub__(self, scalar):
        return self - Vector(scalar, scalar)

    def __getitem__(self, key):#v[key] = v.__getitem__(key)
        if key == "x":
            return self.x
        elif key == "y":
            return self.y
        else:
            raise KeyError("Invalid key")
    
    def __setitem__(self, key, value):# v.__setitem__(key, value)
        if key == "x":
            return Vector(value, self.y)
        elif key == "y":
            return Vector(self.x, value)
        else:
            raise KeyError("Invalid key")

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return self

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)


    def __hash__(self):
        return hash((self.x, self.y))



v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(0,0)
v4 = Vector(2,2)
v = Vector(5, 10)
x, y = v  # Должно работать как распаковка


print(v["x"])
print(len(v4))
print(bool(v3))
print(bool(v1))
print(v1 @ v2)
print(list(Vector(1, 2)))
print(x, y)  # 5 10
print(v1 / 2)
print(len(v1))
print(v1 + v2)  # Ожидаемый результат: Vector(4, 6)
print(v1 - v2)  # Ожидаемый результат: Vector(2, 2)
