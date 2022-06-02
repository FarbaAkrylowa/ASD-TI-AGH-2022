from random import sample
from math import sqrt


def random_path():
    # wartosc dowolnej sciezki
    with open("TSP.txt", "r") as f:
        Cities = f.readlines()
        n = len(Cities)

    for i in range(n):
        Cities[i] = Cities[i].split()
        Cities[i][0] = int(Cities[i][0])
        Cities[i][1] = float(Cities[i][1])
        Cities[i][2] = float(Cities[i][2])

    Path = sample(range(1, n + 1), 100)
    path_len = 0

    for i in range(n - 1):
        x = (Cities[Path[i] - 1][1] - Cities[Path[i + 1] - 1][1]) ** 2
        y = (Cities[Path[i] - 1][2] - Cities[Path[i + 1] - 1][2]) ** 2
        dist = sqrt(x + y)
        path_len += dist

    x = (Cities[Path[n - 1] - 1][1] - Cities[Path[0] - 1][1]) ** 2
    y = (Cities[Path[n - 1] - 1][2] - Cities[Path[0] - 1][2]) ** 2
    path_len += sqrt(x + y)

    return path_len


if __name__ == "__main__":
    for j in range(10):
        print('Sciezka wybrana losowo ' + str(j+1) + ':', random_path())
