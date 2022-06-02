def naive_pattern_find(pattern, text):
    n = len(text)
    m = len(pattern)
    res = []
    for i in range(n-m+1):
        flag = False
        for j in range(m):
            if pattern[j] == text[i+j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            res.append(i)
    print(res)


def rabin_karp_find_pattern(text, pattern):
    d = 16
    q = 101
    n = len(text)
    m = len(pattern)
    p = 0
    t0 = 0
    for i in range(m):
        p = (d * p + pattern[i]) % q
        t0 = (d * t0 + text[i]) % q

    for s in range(n-m+1):
        pass



# def rabin_karp_find_pattern(pattern, text):
#     n = len(text)
#     m = len(pattern)
#     print(n, m)
#     pattern_sum = 0
#     for letter in pattern:
#         if ord(letter) < 65:
#             pattern_sum += int(letter)
#         else:
#             pattern_sum += (ord(letter) - 55)
#     print(pattern_sum)
#
#     sum_ = 0
#     for i in range(m):
#         if ord(text[i]) < 65:
#             sum_ += int(text[i])
#         else:
#             sum_ += (ord(text[i]) - 55)
#     hash_table = [sum_]
#
#     for i in range(1, n-m+1):
#         if ord(text[i - 1]) < 65:
#             sum_ -= int(text[i - 1])
#         else:
#             sum_ -= (ord(text[i - 1]) - 55)
#         if ord(text[i + m - 1]) < 65:
#             sum_ += int(text[i + m - 1])
#         else:
#             sum_ += (ord(text[i + m - 1]) - 55)
#         hash_table.append(sum_)
#     print(n-m-1)
#     print(hash_table)
#     pot_id = []
#     for i in range(len(hash_table)):
#         if pattern_sum == hash_table[i]:
#             pot_id.append(i)
#     pot_id.append(3)
#     print(pot_id)
#     res = []
#     for word in pot_id:
#         flag = False
#         for i in range(m):
#             if text[word+i] == pattern[i]:
#                 flag = True
#             else:
#                 flag = False
#                 break
#         if flag:
#             res.append(word)
#     print(res)


# naive_pattern_find("AABA", "AABAACAADAABAABA")
rabin_karp_find_pattern('ABC', '6EEBF39A1C680CC143ABCF3')
