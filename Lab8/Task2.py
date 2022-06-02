from math import sqrt
import time

from queue import PriorityQueue


class Node:
    def __init__(self, val):
        self.parent = self
        self.value = val
        self.rank = 0


# find, union - zamortyzowane O(1)
def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return


# O(ElogV)
def kruskal(G):
    V = len(G)
    Vertices = [None for i in range(V)]
    Edges = PriorityQueue()  # w postacie (waga, z, do)
    MST = []
    for i in range(V):
        Vertices[i] = Node(i)
    for v in range(V):
        for u in range(v, V):
            if G[u][v] > -1:
                Edges.put((G[v][u], v, u))
    while not Edges.empty():
        weight, u, v = Edges.get()
        x = find(Vertices[u])
        y = find(Vertices[v])
        if x != y:
            MST.append((u, v))
            union(x, y)

    return MST


# O(V^2)
def dfs_matrix(G):
    def DFSVisit(G, u):
        nonlocal visited, vertices
        visited[u] = True
        vertices.append(u)

        for v in range(V):
            if G[u][v] > -1 and not visited[v]:
                DFSVisit(G, v)

    V = len(G)
    visited = [False for _ in range(V)]
    vertices = []

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)

    return vertices


def better_path():
    start_time = time.time()
    with open("TSP.txt", "r") as f:
        Cities = f.readlines()
        V = len(Cities)

    for i in range(V):
        Cities[i] = Cities[i].split()
        Cities[i][0] = int(Cities[i][0])
        Cities[i][1] = float(Cities[i][1])
        Cities[i][2] = float(Cities[i][2])

    # Sciezka w kolejnosci leksykograficznej
    first_order_path = 0
    for i in range(V - 1):
        x = (Cities[i][1] - Cities[i + 1][1]) ** 2
        y = (Cities[i][2] - Cities[i + 1][2]) ** 2
        first_order_path += sqrt(x + y)

    x = (Cities[V - 1][1] - Cities[0][1]) ** 2
    y = (Cities[V - 1][2] - Cities[0][2]) ** 2
    first_order_path += sqrt(x + y)

    # Lepsza sciezka
    # Robimy sobie reprezentacje grafowa
    # Szukamy mst dla naszego grafu
    # Z naszego mst robimy sobie drzewo reprezentowane grafem
    # DFS'em przechodzimy po grafie i w tej kolejnosci potem liczymy dlugosc sciezki

    Graph = [[-1 for i in range(V)] for j in range(V)]

    for v in range(V):
        for u in range(v, V):
            if u != v:
                x = (Cities[v][1] - Cities[u][1]) ** 2
                y = (Cities[v][2] - Cities[u][2]) ** 2
                dist = sqrt(x + y)
                Graph[v][u] = dist
                Graph[u][v] = dist

    MST = kruskal(Graph)
    MST = set(MST)

    for v in range(V):
        for u in range(V):
            if not (v, u) in MST:
                Graph[v][u] = -1

    for v in range(V):
        for u in range(v, V):
            if Graph[v][u] > -1:
                Graph[u][v] = Graph[v][u]

    da_wae = dfs_matrix(Graph)
    print(da_wae)
    print(len(da_wae))
    my_better_path = 0
    for i in range(V-1):
        x = (Cities[da_wae[i]][1] - Cities[da_wae[i+1]][1]) ** 2
        y = (Cities[da_wae[i]][2] - Cities[da_wae[i+1]][2]) ** 2
        my_better_path += sqrt(x + y)

    x = (Cities[da_wae[V-1]][1] - Cities[da_wae[0]][1]) ** 2
    y = (Cities[da_wae[V-1]][2] - Cities[da_wae[0]][2]) ** 2
    my_better_path += sqrt(x + y)

    return first_order_path, my_better_path, time.time() - start_time


if __name__ == "__main__":
    recom_path, my_path, finish = better_path()
    print('Sciezka typu 1 -> 2 -> 3 -> ... -> 100:',  recom_path)
    print('Moja optymalniejsza sciezka: ', my_path)
    print('Czas wykonania sie algorytmu:', finish)
    print('Stosunek pierwszej sciezki 1 - 100 do znalezionej sciezki:', recom_path / my_path)

