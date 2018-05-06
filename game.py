import numpy as np
from matplotlib import pyplot as plt

def init():
    n, m = map(int, input("Board dimensions: ").split())
    r = input("Randomize? [yes/no]: ")
    if r == "yes":
        a = np.random.randint(2, size=(n, m))
    else:
        a = np.zeros((n, m))
        N = int(input("Number of cells to input:  "))
        print("0<=n<{}, 0<=m<{}".format(n, m))
        for k in range(N):
            n_k, m_k = map(int, input().split())
            a[n_k][m_k] = 1
    t = int(input("Time: "))
    return a, t

def countLiveNeighbours(a, n, m):
    N = len(a)
    M = len(a[0])
    live_cells = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                pass #center cell
            else:
                if 0 <= n+i < N and 0 <= m+j < M:
                    if a[n+i][m+j] == 1:
                        live_cells += 1
    return live_cells

def updateBoard(a):
    N = len(a)
    M = len(a[0])
    b = np.zeros((N, M))
    for k in range(N):
        for j in range(M):
            cell = a[k][j]
            live_cells = countLiveNeighbours(a, k, j)
            if cell == 0:
                if live_cells == 3:
                    b[k][j] = 1
            else:
                if live_cells < 2:
                    b[k][j] = 0
                elif live_cells == 2 or live_cells == 3:
                    b[k][j] = 1
                else:
                    b[k][j] = 0 #r >3
    return b

def main():
    board, t = init()
    plt.imshow(board)
    plt.savefig("img0.png")
    plt.cla()
    print("Please wait...")
    for img in range(1, t+1):
        board = updateBoard(board)
        plt.imshow(board)
        plt.savefig("img{}.png".format(img))
        plt.cla()
    print("Done!")
main()      
