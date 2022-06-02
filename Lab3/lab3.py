import zad2_module
import random
import math
import os


def zad1():
    for file in os.listdir("zadanie1"):
        try:
            os.mkdir("zadanie1/" + file[0])
        except FileExistsError:
            pass

        os.rename("zadanie1/" + file, "zadanie1/" + file[0] + "/" + file)


def zad2():
    print("Obwod i pole jakiej figury potrzebujesz obliczyc?")
    print("(kolo, trojkat, kwadrat)")
    figure = str(input())
    print("")

    if figure == "kolo":
        print("Podaj promien kola:")
        r = float(input())
        f1 = zad2_module.Circle(r)
        print("Obwod: ", f1.perimeter())
        print("Pole: ", f1.area())

    elif figure == "trojkat":
        print("Podaj boki trojkata: ")
        a = float(input())
        b = float(input())
        c = float(input())
        f2 = zad2_module.Triangle(a, b, c)
        print("Obwod: ", f2.perimeter())
        print("Pole: ", f2.area())

    elif figure == "kwadrat":
        print("Podaj bok kwadratu:")
        a = float(input())
        f3 = zad2_module.Square(a)
        print("Obwod: ", f3.perimeter())
        print("Pole: ", f3.area())

    else:
        print("Niestety nie mamy takiej figury w bibliotece :(")
        return None


def zad3(r):
    # n_point - liczba losowanych punktów
    # area_points - liczba punktow zawartych w okregu, później używana w obliczaniu całki z sinusa ale wcześniej zerowana
    n_points = int(input("Podaj liczbe puntow: "))
    area_points = 0

    for i in range(n_points):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        dist = math.sqrt(x * x + y * y)
        if dist <= r:
            area_points += 1
    square_area = 2 * r * 2 * r
    cir_area = area_points / n_points * square_area
    print(cir_area)

    # Calka z sinusa na przedziale [0, 2]
    area_points = 0
    for i in range(n_points):
        x = random.uniform(0, 2)
        y = random.uniform(0, 1)
        if y <= math.sin(x):
            area_points += 1
    square_area = 2.0
    sin_area = area_points / n_points * square_area
    print(sin_area)


# zad1()

# Przykładowa funkcja sprawdzająca czy stworzony moduł z zadania 2 działa
# zad2()

# zad3(1.0)
