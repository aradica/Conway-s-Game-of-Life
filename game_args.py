import argparse
import numpy as np
from matplotlib import pyplot as plt

def countLiveNeighbours(a, n, m, N, M):
    live_cells = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                pass #center cell
            else:
                if 0 <= n+i < N and 0 <= m+j < M:
                    if a[n+i, m+j] == 1:
                        live_cells += 1
    return live_cells

def countLiveCells(a):
    population = 0
    for k in a:
        for j in k:
            if j == 1:
                population += 1
    return population

def countLiveCellsFast(a, N, M):
    return N*M - np.sum(a, dtype=np.int32)

def updateBoard(a, N, M):
    b = np.zeros((N, M))
    for k in range(N):
        for j in range(M):
            cell = a[k,j]
            live_cells = countLiveNeighbours(a, k, j, N, M)
            if cell == 0:
                if live_cells == 3:
                    b[k,j] = 1
            else:
                if live_cells < 2:
                    b[k,j] = 0
                elif live_cells == 2 or live_cells == 3:
                    b[k,j] = 1
                else:
                    b[k,j] = 0 #r >3
    return b

def updateBoardFast(a, N, M):
    b = np.zeros((N, M))
    for k, row in enumerate(a):
        for j, cell in enumerate(row):
            live_cells = countLiveNeighbours(a, k, j, N, M)
            if cell == 0:
                if live_cells == 3:
                    b[k, j] = 1
            else:
                if live_cells < 2:
                    b[k, j] = 0
                elif live_cells == 2 or live_cells == 3:
                    b[k, j] = 1
                else:
                    b[k, j] = 0
    return b
                             

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--rows", required=True, help="rows")
    ap.add_argument("-m", "--collumns", required=True, help="collumns")
    ap.add_argument("-p", "--percentage", required=True, help="percentage of live cells")
    ap.add_argument("-t", "--time", required=True, help="time")
    ap.add_argument("-s", "--save", required=True, help="save images")
    ap.add_argument("-l", "--live", required=True, help="show live updates")
    args = vars(ap.parse_args())

    N, M, pcnt, t, s, l = int(args["rows"]), int(args["collumns"]), int(args["percentage"]) / 100, int(args["time"]), args["save"], args["live"]
    board = np.random.choice([0, 1], size=(N,M), p=[1-pcnt, pcnt])
    
    pgraph = []
    
    print("Working on it...")
    IMG = plt.imshow(board,cmap='gray')
    for img in range(t):
        IMG.set_data(board)

        P = countLiveCellsFast(board, N, M)
        pgraph.append(P)
        plt.title("Time: {}, Cells: {}".format(img,P))
        if s == "1":
            plt.savefig("Imgs/img{}.png".format(img),bbox_inches='tight')
        board = updateBoardFast(board, N, M)
        if l == "1":
            plt.pause(0.005)
    if l == "1":
        plt.show()
    plt.cla()
    print("Done!")
    plt.plot([x for x in list(range(t))], pgraph)
    plt.title('{}x{}'.format(N, M))
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title
    plt.savefig("Imgs/graph.png")
    plt.show()

main()
