"""
Alphabet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}
TODO: Zmienic Rabina Karpa
"""
import time


def naive_find_2d(n):
    with open(str(n) + "_pattern.txt", "r") as f:
        Text = f.readlines()
        pattern = 'ABC'
        start_time = time.time()
        n = len(Text)
        m = len(pattern)
        res = []
        for row in range(n - m + 1):  # idziemy po wierszach
            for letter in range(n - m + 1):  # idziemy po kazdej literce w danym wierszu
                # Zakomentowana wersja bardziej uniwersalna, gdyby wzorzec wygladal inaczej
                # flag = False
                # for i in range(m):
                #     if pattern[0][i] == Text[row][letter + i] and pattern[1][i] == Text[row + i][letter]:
                #         flag = True
                #     else:
                #         flag = False
                #         break
                # if flag:
                #     res.append((row, letter))
                if Text[row][letter] == 'A' and Text[row][letter + 1] == Text[row + 1][letter] == 'B' \
                        and Text[row][letter + 2] == Text[row + 2][letter] == 'C':
                    res.append((row, letter))
        print('Czas wykonania calego algorytmu:', time.time() - start_time)

    return len(res)


def rabin_karp_2d(n):
    # argumenty (patter, text, q=prime number, d=len(alphabet))
    with open(str(n) + "_pattern.txt", "r") as f:
        Text = f.readlines()
        pattern = 'ABC'
        start_time = time.time()
        preprocessing_start = time.time()
        n = len(Text[0])
        m = len(pattern)
        hash_table = [[] for row in range(n-m)]
        potential_ids = []
        res = []

        pattern_sum = 0
        for letter in pattern:
            if ord(letter) < 65:
                pattern_sum += int(letter)
            else:
                pattern_sum += (ord(letter) - 55)

        for row in range(n - m):
            sum1 = 0
            for i in range(m):
                if ord(Text[row][i]) < 65:
                    sum1 += int(Text[row][i])
                else:
                    sum1 += (ord(Text[row][i]) - 55)
            hash_table[row].append(sum1)

            for i in range(1, n - m):
                if ord(Text[row][i - 1]) < 65:
                    sum1 -= int(Text[row][i - 1])
                else:
                    sum1 -= (ord(Text[row][i - 1]) - 55)
                if ord(Text[row][i + m - 1]) < 65:
                    sum1 += int(Text[row][i + m - 1])
                else:
                    sum1 += (ord(Text[row][i + m - 1]) - 55)
                hash_table[row].append(sum1)
        preprocessing_end = time.time() - preprocessing_start

        find_pattern_start = time.time()
        for x in range(len(hash_table)):
            for y in range(len(hash_table[x])):
                if hash_table[x][y] == pattern_sum:
                    potential_ids.append((x, y))

        for x, y in potential_ids:
            flag = False
            for i in range(m):
                if pattern[i] == Text[x][y + i] and pattern[i] == Text[x + i][y]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                res.append((x, y))
        find_pattern_end = time.time() - find_pattern_start

        end_of_alg = time.time() - start_time
        print('Czas wykonania calego alogorytmu:', end_of_alg)
        print('Czas wykonania preprocessingu:', preprocessing_end)
        print('Czas szukania wzorca:', find_pattern_end)

        return len(res)


'''
Set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A=10, B=11, C=12, D=13, E=14, F=15
ord(A-F) - 55
'''

if __name__ == "__main__":
    sizes = [1000, 2000, 3000, 4000, 5000, 8000]
    for size in sizes:
        print('===', size, '===')
        print('Naiwne podejscie')
        a = naive_find_2d(size)
        print('Rabin Karp')
        b = rabin_karp_2d(size)
        print('Wyniki obu algorytmow: ', a, b)
        print()
