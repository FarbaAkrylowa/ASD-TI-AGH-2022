import time


def rec_number_of_moves_Hanoi(n):
    def Hanoi(n, sour, dest, buff):
        nonlocal moves
        if n == 1:
            moves += 1
            print("Move disk", n, "from", sour, "to", dest)
            return

        Hanoi(n - 1, sour, buff, dest)
        print("Move disk", n, "from", sour, "to", dest)
        moves += 1
        Hanoi(n - 1, buff, dest, sour)

    moves = 0
    start_time = time.time()
    Hanoi(n, 'A', 'B', 'C')
    print(moves)
    print("Czas rekurencji:", time.time() - start_time)


def iter_number_of_moves_Hanoi(n, sour, dest, buff):
    Hanoi = []
    moves = 0
    start_time = time.time()
    while n > 0 or len(Hanoi) != 0:
        while n > 0:
            cur_sour = sour
            cur_buff = buff
            cur_dest = dest
            cur_n = n
            Hanoi.append((cur_n, cur_sour, cur_buff, cur_dest))
            dest, buff = buff, dest
            n -= 1

        cur_n, cur_sour, cur_buff, cur_dest = Hanoi.pop()
        print("Move disk", cur_n, "from", cur_sour, "to", cur_dest)
        if cur_n >= 1:
            moves += 1
            sour = cur_buff
            buff = cur_sour
            dest = cur_dest
            n = cur_n - 1
    print(moves)
    print("Czas iteracji:", time.time() - start_time)


rec_number_of_moves_Hanoi(7)
iter_number_of_moves_Hanoi(7, 'A', 'B', 'C')
