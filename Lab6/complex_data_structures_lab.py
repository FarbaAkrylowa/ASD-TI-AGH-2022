import random
import time


def binary_search(T, l, r, elem, ret_id):
    while l <= r:
        mid = (l + r) // 2
        if elem > T[mid].val:
            l = mid + 1
        elif elem < T[mid].val:
            r = mid - 1
        else:
            return mid
    if ret_id:
        return l


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None

    def insert_data(self, elem):
        # wstawiamy element do niepustego drzewa, nie będzie puste, bo jeżeli tak będzie to pierwszy element
        # będzie dodany wczesniej
        y = None
        x = self
        while x is not None:
            y = x
            if elem.val < x.val:
                x = x.left
            else:
                x = x.right
        elem.parent = y
        if elem.val < y.val:
            y.left = elem
        else:
            y.right = elem

    def minimum_of_tree(self):
        root = self
        while root.left is not None:
            root = root.left
        return root

    def maximum_of_tree(self):
        root = self
        while root.right is not None:
            root = root.right
        return root

    def search_node(self, elem):
        root = self
        while root is not None:
            if root.val == elem:
                return True
            elif root.val > elem:
                root = root.left
            else:
                root = root.right
        return False

    def print_tree(self, depth, newline):
        if newline:
            print('\n' + '\t' * depth + '-' * depth + str(self.val) + '\t', end='')
        else:
            print('-' * depth + str(self.val) + '\t', end='')

        if self.left:
            self.left.print_tree(depth + 1, False)

        if self.right:
            self.right.print_tree(depth + 1, True)


class NodesArray:
    def __init__(self):
        self.list = []

    def insert_new_node(self, elem):
        found = self.search(elem)
        if found:
            return None
        else:
            n = len(self.list)
            pot_root = round(elem)
            if elem - pot_root >= 0:
                pot_root += 0.5
            else:
                pot_root -= 0.5

            pot_index = binary_search(self.list, 0, n - 1, pot_root, True)
            if pot_index >= n:
                self.list.append(Node(pot_root))
                self.list[pot_index].insert_data(Node(elem))
            else:
                if pot_root == self.list[pot_index].val:
                    self.list[pot_index].insert_data(Node(elem))
                else:
                    self.list.insert(pot_index, Node(pot_root))
                    self.list[pot_index].insert_data(Node(elem))

    def minimum(self, root):
        min_ = root.minimum_of_tree()
        return min_

    def maximum(self, root):
        max_ = root.maximum_of_tree()
        return max_

    def search(self, elem):
        n = len(self.list)
        if n != 0:
            pot_root = round(elem)
            if elem - pot_root >= 0:
                pot_root += 0.5
            else:
                pot_root -= 0.5

            pot_id = binary_search(self.list, 0, n - 1, pot_root, False)
            if pot_id is None:
                return False
            if pot_root == self.list[pot_id].val:
                return self.list[pot_id].search_node(elem)
            else:
                return False
        else:
            return False

    def print(self):
        for x in self.list:
            x.print_tree(0, False)
            print('\n')


def podpunkt_1(T):
    Arr = NodesArray()
    for x in T:
        Arr.insert_new_node(x)
    return Arr


def podpunkt_2(T):
    print('Dodajemy element 7.4 i 10.24, a nastepnie printujemy drzewo, zeby sprawdzic czy faktycznie zostal dodany')
    T.insert_new_node(7.4)
    T.insert_new_node(10.24)
    T.print()

    print('Element minimalny drzewa o korzeniu 7.5 - drzewo w tablicy o indeksie 3')
    print(T.minimum(T.list[3]).val)
    print('Element maksymalny drzewa o korzeniu 7.5 - drzewo w tablicy o indeksie 3')
    print(T.maximum(T.list[3]).val)

    print('Sprawdzamy czy element jest w strukturze')
    print('Czy 8.4 w strukturze:', T.search(8.4))
    print('Czy 7.9 w strukturze:', T.search(7.9))


def podpunkt_3(n):
    function_start = time.time()
    print('n =', n)
    item_to_find = None
    T = [0.0 for _ in range(n)]
    for i in range(n):
        T[i] = round(random.uniform(0.50, 50.50), 2)
        if i == n//2:
            item_to_find = T[i]
    Our_structure = podpunkt_1(T)

    start_time = time.time()
    Our_structure.insert_new_node(29.79)
    print("Insert: ", time.time() - start_time)

    start_time = time.time()
    ind = random.randint(0, len(Our_structure.list) - 1)
    Our_structure.minimum(Our_structure.list[ind])
    print("Minimum: ", time.time() - start_time)

    start_time = time.time()
    ind = random.randint(0, len(Our_structure.list) - 1)
    Our_structure.maximum(Our_structure.list[ind])
    print("Maximum: ", time.time() - start_time)

    start_time = time.time()
    Our_structure.search(item_to_find)
    print("Search: ", time.time() - start_time)

    print("Czas funkcji: ", time.time() - function_start)


# if __name__ == "__main__":
#     # Podpunkt 1
#     print("Podpunkt 1")
#     Tab = [7.3, 7.8, 9.3, 3.7, 1.3, 7.7, 7.9, 4.0, 4.99, 1.6, 7.6, 7.7]
#     New_data_structure = podpunkt_1(Tab)
#     New_data_structure.print()
#     print('\n')
#
#     # Podpunkt 2
#     print("Podpunkt 2")
#     podpunkt_2(New_data_structure)
#     print('\n')
#
#     # Podpunkt 3
#     # print("Podpunkt 3")
#     # podpunkt_3(25)
#     # print('\n')
#     # podpunkt_3(50)
#     # print('\n')
#     # podpunkt_3(100)
#     # print('\n')
#     # podpunkt_3(500)
#     # print('\n')
#     # podpunkt_3(1000000)
#     print("hello")
