import numpy as np

puzzle = [[0, 0, 0, 8, 0, 5, 4, 2, 7],
        [0, 0, 7, 2, 0, 3, 9, 0, 5],
        [0, 2, 4, 7, 0, 1, 0, 0, 0],
        [7, 4, 0, 0, 8, 6, 1, 0, 0],
        [0, 0, 8, 9, 1, 0, 7, 0, 4],
        [0, 1, 0, 0, 3, 0, 0, 9, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 1, 3, 7, 0, 0, 0, 6],
        [2, 0, 0, 0, 5, 0, 3, 0, 0]]


def possible(y,x,n):
    global puzzle
    for i in range(0, 9):
        if puzzle[y][i] == n:
            return False
    for i in range(0,9):
        if puzzle[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0, 3):
            if puzzle[y0 + 1][x0 + j] == n:
                return False
    return True


def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        solve()
                        puzzle[y][x] = 0
                return
    print(np.matrix(puzzle))
    input("Another possibility? (press enter)")

solve()
