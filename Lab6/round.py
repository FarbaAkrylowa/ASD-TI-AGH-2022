# x = 6.5
# y = 6.51
# z = 6.49
# print(round(x))
# print(round(y))
# print(round(z))
#
# A = [0, 3, 2, 1]
# print(A)
# A.insert(1, 69)
# print(A)

'''
round() działa tak, że jeżeli coś jest mniejsze lub równe połowie to zaokrągla w dół, w przeciwnym wypadku w górę
insert(gdzie, co) dodaje nowy element do listy pod dany indeks
'''


# binary search, ale jeżeli nie ma danego elementu to zwraca indeks, pod którym powinien się element znajdować
def binary_search(T, l, r, elem):
    while l <= r:
        mid = (l + r) // 2
        if elem > T[mid]:
            l = mid + 1
        elif elem < T[mid]:
            r = mid - 1
        else:
            return mid
    return l

#
# L = [0, 1, 2, 3, 5, 6]
# R = [0, 1, 2, 5, 6]
# print(binary_search(L, 0, len(L) - 1, 5.5))
# print(binary_search(R, 0, len(R) - 1, -1))
# # jeśli nie ma, a len jest parzysta to zwracamy l, jeśli nieparzyste to też l
# C = []
# print(binary_search(C, 0, len(C) - 1, -1))
# # jesli nie ma nic zapisanego to zwraca 0
#
# print(round(3.7))


B = [1.5]
print(binary_search(B, 0, len(B) - 1, 3.5))

