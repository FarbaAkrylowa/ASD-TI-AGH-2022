# zad2_module
from math import pi
from math import sqrt


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * self.r * self.r


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return self.a + self.b + self.c
        else:
            print("Taki trojkat nie istnieje")
            return None

    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            p = (self.a + self.b + self.c) / 2
            return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            print("Taki trojkat nie istnieje")
            return None


class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a * self.a
