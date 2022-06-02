"""
Alphabet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}
"""
import time


def rabin_karp_2d(n):
    # 1 - szukamy mozliwych poczatkow dla kazdego wiersza
    # 2 - jak dostaniemy tablice z mozliwymi wynikami to
    # pozniej sprawdzamy odpowiednie wsporzedne zwyklym ifem albo forem
    with open(str(n) + "_pattern.txt", "r") as f:
        Text = f.readlines()
        pattern = 'ABC'
        start_time = time.time()
        n = len(Text[0])
        m = len(pattern)
        potential_ids = []
        res = []
        hash_table = [[] for row in range(n-m)]

        pattern_sum = 0                 # liczymy sume naszego wzorca
        for letter in pattern:
            if ord(letter) < 65:
                pattern_sum += 2 * int(letter)
            else:
                pattern_sum += 2 * (ord(letter) - 55)

        if ord(pattern[0]) < 65:
            pattern_sum -= int(pattern[0])
        else:
            pattern_sum -= (ord(pattern[0]) - 55)

        for row in range(n-m):                  # poziome sumy
            sum_ = 0
            for i in range(m):
                if ord(Text[row][i]) < 65:
                    sum_ += int(Text[row][i])
                else:
                    sum_ += (ord(Text[row][i]) - 55)

            hash_table[row].append(sum_)

            for letter in range(n-m):
                pass

        for row in range(n-m):                  # pionowe sumy
            for letter in range(n-m):
                pass


                hash_table[row].append(sum_)


        return len(res)


'''
Set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A=10, B=11, C=12, D=13, E=14, F=15
ord(A-F) - 55
'''
rabin_karp_2d(1000)
