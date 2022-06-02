import time


def Zadanie1():
    res = ''
    # 500, 501, 502, 503 sa niepodzielne przez 7, zaczynamy od 504
    for i in range(504, 3001, 7):
        if i % 5 != 0:
            c = str(i)
            res = res + c

    print(res)  # Wypisanie polaczonego stringa wynikow
    c = res.count('21')
    new_res = res.replace('21', 'XX')
    print(new_res)
    print("Liczba ciagu 21: ", c)


def Zadanie2():
    # Wczytanie pliku
    file = open('zadanie2.csv', 'r')
    lines = file.readlines()

    # Usuwanie linii bez wartosci val   --> O(n)
    proceeded_file = []
    for l in lines:
        l = l.split(",", 1)
        if l[1] != '\n':
            proceeded_file.append(l)

    # Sortowanie pliku wzgledem wartosci id     --> O(n + nlogn) = O(nlogn), n bierze sie ze slicingu
    proceeded_file[1:] = sorted(proceeded_file[1:], key=lambda x: int(x[0]))

    # Usuwanie duplikatow
    for i in range(2, len(proceeded_file)):
        prev = int(proceeded_file[i - 1][0])
        curr = int(proceeded_file[i][0])
        if prev >= curr:
            curr = prev + 1
            wstaw = str(curr)
            proceeded_file[i][0] = wstaw

    # Zamiana duzych liter na male  --> O(n*k) k - dlugosc stringa
    for l in proceeded_file:
        l[1] = l[1].lower()

    # Usuwanie wyrazow z dwuliterowym prefiksem, ktorych litery sa obok siebie w ASCII
    for l in proceeded_file:
        approved_words = []
        sentence = l[1].split()
        for s in sentence:
            if len(s) >= 2 and abs(ord(s[0]) - ord(s[1])) == 1:
                print("Usunieto: ", s)
            else:
                approved_words.append(s)
        print("")
        l[1] = " ".join(approved_words)

    file.close()


# Ta wersja uzywa zwyklego przejscia po calym pliku i sprawdza kazdy wyraz do znalezienia szukanego
# Zlozonosc to chyba O(nk), k to dlugosc aktualnie przetwarzanego wyrazu w metodzie string.strip() usuwajacej znak
# nowej linii
def Zadanie3():
    # Wczytanie wyrazu
    word = str(input("Podaj wyraz: "))

    # Sprawdzenie czy jest to jeden wyraz. Zakladam, ze jezeli podany wyraz konczy sie pustym znakiem (np. spacja)
    # to jest to niepoprawnie podany wyraz do sprawdzenia
    start_time = time.time()
    for letter in word:
        if letter == " ":
            print("To nie jest jeden wyraz")
            return 0

    # Sprowadzenie wyrazu to zapisu z uzyciem samych liter
    word = word.lower()

    # Sprawdzanie czy wyraz nalezy do slownika, trzeba uwazac bo na koncu kazdego wyrazu jest \n, ja o tym na poczatku
    # nie pomyslalem i mialem problemy jak to rozwiazac
    SJP = open('SJP.txt', 'r', encoding='utf-8')

    for l in SJP:                                   # Na ten moment O(n * max_len(words))
        if l.strip('\n') == word:
            print("Slowo", word, "jest w slowniku")
            break
    else:
        print("Slowo", word, "nie jest w slowniku")

    SJP.close()
    print("Czas prztwarzania: ", time.time() - start_time)


# Ta wersja uzywa binary searcha do szukania slowa, jej zlozonosc to chyba O(klogn), k - dlugosc przetwarzanego wyrazu
# k bierze sie z metody string.strip() usuwajacej znaki nowej linii, a logn to zlozonosc binary searcha na n elementowej
# tablicy
def Zadanie3_improved():
    word = str(input("Podaj wyraz: "))      # <- wczyatnie wyrazu

    start_time = time.time()
    for letter in word:     # <- sprawdzanie czy to jest jeden wyraz
        if letter == " ":
            print("To nie jest jeden wyraz")
            return 0
    word = word.lower()     # <- usuwanie wielkich liter

    SJP = open('SJP.txt', 'r', encoding='utf-8')
    tab_SJP = SJP.readlines()                       # <- stworzenie tablicy do uzycia binary searcha

    # Binary search
    flag = False
    left = 0
    right = len(tab_SJP) - 1
    while left <= right:
        ind = (left + right) // 2
        if tab_SJP[ind].strip() < word:
            left = ind + 1
        elif tab_SJP[ind].strip() > word:
            right = ind - 1
        else:
            print("Slowo", word, "jest w slowniku")
            flag = True
            break

    if not flag:
        print("Slowo", word, "nie jest w slowniku")

    SJP.close()
    print("Czas prztwarzania: ", time.time() - start_time)


print("Zadanie 1")
# Zadanie1()
print("Zadanie 2")
# Zadanie2()
print("Zadanie 3")
# Zadanie3()
print("Zadanie3_improved")
# Zadanie3_improved()
