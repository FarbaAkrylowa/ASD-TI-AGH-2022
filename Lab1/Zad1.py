import time
from array import *
import random


def Zad1():
    # Generowanie listy
    start_time = time.time()
    L = list()
    L.append(1.0)
    L.append(2.0)

    for i in range(2, 48):
        L.append((L[i - 1] + L[i - 2]) / (L[i - 1] - L[i - 2]))

    print("Lista: ", end="")
    print(L)

    # Srednia i moda
    L.sort()
    print("Posortowana lista: ", L)
    s = 0
    for i in L:
        s += i
    avg = s / 48.0
    print("Srednia: ", avg)

    count = 1
    mode = L[0]
    curr_count = 1
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            curr_count += 1
            if curr_count > count:
                count = curr_count
                mode = L[i]

    if count == 1:
        print("Brak dominanty")
    else:
        print("Moda: ", mode)

    # Szukanie powtorzonych elementow
    p = False
    i = 0
    while i < len(L) - 1:
        if L[i] == L[i + 1]:
            p = True
            print("Powtorzona wartosc: ", L[i])
            while L[i] == L[i + 1]:
                i += 1
        i += 1
    if not p:
        print("Brak powtorzonych wartosci")
    full_time = time.time() - start_time
    print("Czas dzialania Zad1: ", full_time)


def Zad2():
    start_time = time.time()
    A = array('f')
    A.append(1.0)
    A.append(2.0)
    for i in range(2, 48):
        A.append((A[i - 1] + A[i - 2]) / (A[i - 1] - A[i - 2]))
    print("Tablica: ", A)
    # Sortowanie tablicy zeby obliczyc dominante
    for i in range(len(A) - 1):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print("Posortowana tablica: ", A)
    # Srednia
    avg = 0
    for i in A:
        avg += i
    print("Srednia: ", avg / len(A))

    # Dominanta
    count = 1
    mode = A[0]
    curr_count = 1
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            curr_count += 1
            if curr_count > count:
                count = curr_count
                mode = A[i]

    if count == 1:
        print("Brak dominanty")
    else:
        print("Moda: ", mode)

    # Powtorzone wartosci
    p = False
    i = 0
    while i < len(A) - 1:
        if A[i] == A[i + 1]:
            p = True
            print("Powtorzona wartosc: ", A[i])
            while A[i] == A[i + 1]:
                i += 1
        i += 1
    if not p:
        print("Brak powtorzonych wartosci")

    full_time = time.time() - start_time
    print("Czas dzialania Zad2: ", full_time)


def Zad3():
    n = int(input("Podaj n: "))
    A = [None] * n
    A[0] = 1
    A[1] = 1
    s = 0
    for i in range(2, n):
        A[i] = A[i - 1] + A[i - 2]
    print(A)

    start = time.time()
    for i in A:
        s += i
    print("Suma1: ", s)
    print(time.time() - start)

    s = 0
    start = time.time()
    for i in range(len(A)):
        s += A[i]
    print("Suma2: ", s)
    print(time.time() - start)
    # Technicznie czas wykonania wypisany w kocoli jest taki sam, ale nie wiem czy to nie jest zbyt prosty kot na weryfikacje


def Zad4():
    # IndexError
    T = ["Ala", "ma", "kota"]
    try:
        print(T[3])
    except IndexError:
        print("A gdzie to sie tak za tablice wychodzi?")

    # ZeroDivisionError
    a = 7
    b = 0
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Nie dziel prze zero ty jasna...")

    # NameError
    try:
        print(name)
    except NameError:
        print("Kolego, a co to za zmienna?")
    print("Koniec zadania 4")


def Zad5_person_vs_person():
    # Tic-Tac_Toe
    def print_available_moves_board():
        print("Gra polega na podaniu odpowiedniego indeksu gdzie zaznaczyc swoj znak.")
        print("Aby podac gdzie pstawic znak podaj odpowiedni indeks (mozliwe indeksy podane na pierwszej planszy).")
        print("-------------")
        print("|", 0, "|", 1, "|", 2, "|")
        print("-------------")
        print("|", 3, "|", 4, "|", 5, "|")
        print("-------------")
        print("|", 6, "|", 7, "|", 8, "|")
        print("-------------")

    def print_current_board(moves):
        print("-------------")
        print("|", moves[0], "|", moves[1], "|", moves[2], "|")
        print("-------------")
        print("|", moves[3], "|", moves[4], "|", moves[5], "|")
        print("-------------")
        print("|", moves[6], "|", moves[7], "|", moves[8], "|")
        print("-------------")

    def get_move(moves, player):
        print("Podaj indeks pola: ", end="")
        move = int(input())
        moves[move] = player

    def result(moves):
        # |0|1|2|3|4|5|6|7|8|9|
        # Mozliwe kombinacje wygranej:
        # 0,1,2 ; 3,4,5 ; 6,7,8 ; 0,3,6 ; 1,4,7 ; 2,5,8 ; 0,4,8 ; 2,4,6
        if moves[0] == moves[1] and moves[0] == moves[2]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[3] == moves[4] and moves[3] == moves[5]:
            if moves[3] == 'X':
                return False
            elif moves[3] == "O":
                return False
            else:
                return True
        if moves[6] == moves[7] and moves[6] == moves[8]:
            if moves[6] == 'X':
                return False
            elif moves[6] == "O":
                return False
            else:
                return True
        if moves[0] == moves[3] and moves[0] == moves[6]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[1] == moves[4] and moves[1] == moves[7]:
            if moves[1] == 'X':
                return False
            elif moves[1] == "O":
                return False
            else:
                return True
        if moves[2] == moves[5] and moves[2] == moves[8]:
            if moves[2] == 'X':
                return False
            elif moves[2] == "O":
                return False
            else:
                return True
        if moves[0] == moves[4] and moves[0] == moves[8]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[2] == moves[4] and moves[2] == moves[6]:
            if moves[2] == 'X':
                return False
            elif moves[2] == "O":
                return False
            else:
                return True

        return True

    def can_you_move(moves):
        for i in moves:
            if i == ' ':
                return True
        return False

    # actual code
    # W grze niestety nie ma zaimplementowanego sprawdzania bledow, ale gra 1 vs 1 jest jak najbardziej mozliwa,
    # o ile obie druzyny przestrzegaja zasad podanych na poczatku ;)
    game = True
    print_available_moves_board()
    tab_board = [' '] * 9
    print_current_board(tab_board)
    while game:
        get_move(tab_board, 'O')
        game = result(tab_board)
        print_current_board(tab_board)
        if game is False:
            print("Koniec gry!")
            print("Wygral gracz: ", 'O')
            break

        if not can_you_move(tab_board):
            print("Remis, nikt nie wygral!")
            break

        get_move(tab_board, 'X')
        game = result(tab_board)
        print_current_board(tab_board)
        if game is False:
            print("Koniec gry!")
            print("Wygral gracz: ", 'X')
            break


def Zad5_person_vs_AI():
    # Tic-Tac_Toe
    def print_available_moves_board():
        print("Gra polega na podaniu odpowiedniego indeksu gdzie zaznaczyc swoj znak.")
        print("Aby podac gdzie pstawic znak podaj odpowiedni indeks (mozliwe indeksy podane na pierwszej planszy).")
        print("-------------")
        print("|", 0, "|", 1, "|", 2, "|")
        print("-------------")
        print("|", 3, "|", 4, "|", 5, "|")
        print("-------------")
        print("|", 6, "|", 7, "|", 8, "|")
        print("-------------")

    def print_current_board(moves):
        print("-------------")
        print("|", moves[0], "|", moves[1], "|", moves[2], "|")
        print("-------------")
        print("|", moves[3], "|", moves[4], "|", moves[5], "|")
        print("-------------")
        print("|", moves[6], "|", moves[7], "|", moves[8], "|")
        print("-------------")

    def get_move(moves, player):
        print("Podaj indeks pola: ", end="")
        move = int(input())
        moves[move] = player

    def result(moves):
        # |0|1|2|3|4|5|6|7|8|9|
        # Mozliwe kombinacje wygranej:
        # 0,1,2 ; 3,4,5 ; 6,7,8 ; 0,3,6 ; 1,4,7 ; 2,5,8 ; 0,4,8 ; 2,4,6
        if moves[0] == moves[1] and moves[0] == moves[2]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[3] == moves[4] and moves[3] == moves[5]:
            if moves[3] == 'X':
                return False
            elif moves[3] == "O":
                return False
            else:
                return True
        if moves[6] == moves[7] and moves[6] == moves[8]:
            if moves[6] == 'X':
                return False
            elif moves[6] == "O":
                return False
            else:
                return True
        if moves[0] == moves[3] and moves[0] == moves[6]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[1] == moves[4] and moves[1] == moves[7]:
            if moves[1] == 'X':
                return False
            elif moves[1] == "O":
                return False
            else:
                return True
        if moves[2] == moves[5] and moves[2] == moves[8]:
            if moves[2] == 'X':
                return False
            elif moves[2] == "O":
                return False
            else:
                return True
        if moves[0] == moves[4] and moves[0] == moves[8]:
            if moves[0] == 'X':
                return False
            elif moves[0] == "O":
                return False
            else:
                return True
        if moves[2] == moves[4] and moves[2] == moves[6]:
            if moves[2] == 'X':
                return False
            elif moves[2] == "O":
                return False
            else:
                return True

        return True

    def can_you_move(moves):
        for i in moves:
            if i == ' ':
                return True
        return False

    def get_pc_move(moves):
        while True:
            pc_move = random.randint(0, 8)
            if moves[pc_move] == ' ':
                moves[pc_move] = 'X'
                break


    # actual code
    # W grze niestety nie ma zaimplementowanego sprawdzania bledow, ale gra z najbardziej prymitywnym AI jest jak najbardziej mozliwa,
    # o ile obie druzyny przestrzegaja zasad podanych na poczatku ;)
    game = True
    print_available_moves_board()
    tab_board = [' '] * 9
    print_current_board(tab_board)
    while game:
        get_move(tab_board, 'O')
        game = result(tab_board)
        print_current_board(tab_board)
        if game is False:
            print("Koniec gry!")
            print("Wygral gracz: ", 'O')
            break

        if not can_you_move(tab_board):
            print("Remis, nikt nie wygral!")
            break

        get_pc_move(tab_board)
        game = result(tab_board)
        print_current_board(tab_board)
        if game is False:
            print("Koniec gry!")
            print("Wygral gracz: ", 'X')
            break


# print("Zad1")
# Zad1()
# print("Zad2")
# Zad2()
# print("Zad3")
# Zad3()
# print("Zad4")
# Zad4()
# print("Zad5 - Czlowiek vs Czlowiek")
# Zad5_person_vs_person()
print("Zad5 - Czlowiek vs Komputer")
Zad5_person_vs_AI()
