'''
Insertion Sort vs Merge Sort
'''
import time
import random
from sys import maxsize as inf


def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def merge_sort(T):
    def merge(A, p, q, r):
        n1 = q - p
        n2 = r - q

        left = [0 for _ in range(n1+1)]
        right = [0 for _ in range(n2+1)]

        for i in range(n1):
            left[i] = A[p+i]

        for i in range(n2):
            right[i] = A[q+i]

        left[n1] = inf
        right[n2] = inf

        i = j = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1

    def merge_sort_rec(A, p, r):
        if p < r - 1:
            q = (p + r) // 2
            merge_sort_rec(A, p, q)
            merge_sort_rec(A, q, r)
            merge(A, p, q, r)

    merge_sort_rec(T, 0, len(T))


def generate_tab(size):
    L = [random.randint(0, 1000) for _ in range(size)]
    return L


def sort_comparison():
    # Testowanie Insertion Sortas
    min_time = inf
    max_time = -1
    avg_time = iter_time = 0
    for i in range(100):
        start_iter = time.time()
        A = generate_tab(10000)
        start_t = time.time()
        insertion_sort(A)
        end_t = time.time() - start_t
        avg_time += end_t
        if end_t < min_time:
            min_time = end_t
        if end_t > max_time:
            max_time = end_t
        iter_time += time.time() - start_iter
    print("Insertion Sort:")
    print("Max: ", max_time)
    print("Min: ", min_time)
    print("Average: ", avg_time / 100)
    print("Full iter time: ", iter_time)

    # Testowanie Merge Sorta
    min_time = inf
    max_time = -1
    avg_time = iter_time = 0
    for i in range(100):
        start_iter = time.time()
        A = generate_tab(100000)
        start_t = time.time()
        merge_sort(A)
        end_t = time.time() - start_t
        avg_time += end_t
        if end_t < min_time:
            min_time = end_t
        if end_t > max_time:
            max_time = end_t
        iter_time += time.time() - start_iter
    print("Merge Sort: ")
    print("Max: ", max_time)
    print("Min: ", min_time)
    print("Average: ", avg_time / 100)
    print("Full iter time: ", iter_time)


sort_comparison()
