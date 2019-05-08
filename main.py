# Conway's Game of Life
import tkinter as tk
from time import sleep
from threading import Thread


# Logic part
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[0 for _ in range(columns)]for _ in range(rows)]

    def countLiveNeighbours(self, row, column):
        fields = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
        alive = 0
        for i, j in fields:
            if 0 <= row+i < self.rows and 0 <= column+j < self.columns:
                if self.board[row+i][column+j] == 1:
                    alive += 1
        return alive

    def countLiveCells(self):
        alive = 0
        for row in self.board:
            for cell in row:
                if cell:
                    alive += 1

        return alive

    def update(self):
        board = [[0 for _ in range(self.columns)]for _ in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                live_cells = self.countLiveNeighbours(row, column)
                if self.board[row][column]:
                    if live_cells == 3:
                        board[row][column] = 1
                else:
                    if live_cells == 2 or live_cells == 3:
                        board[row][column] = 1
        self.board = board

    def show(self):
        for row in self.board:
            print(row)
        print()


# Gui stuff

class Tile:
    def __init__(self, root):
        self.state = 0
        self.button = tk.Button(root, bg="slate blue", command=self.onClick)
        # strange, this is a square...
        self.button.configure(height=2, width=4)

    def onClick(self):
        if self.state:
            self.button.configure(bg="slate blue")
            self.state = 0

        else:
            self.button.configure(bg="snow")
            self.state = 1

        # info = self.button.grid_info()
        # print(info.get("row"), info.get("column"))


# Putting it all togheter

class App:
    def __init__(self):
        # TODO - parametrize this
        rows = 9
        columns = 9

        self.game = Board(rows, columns)
        self.root = tk.Tk()

        self.root.title("Conway's Game of Life")
        self.centerWindow()

        self.gamePanel = tk.Frame(self.root)
        self.gamePanel.pack()
        self.gui = self.makeGrid(self.gamePanel)

        self.cmdPanel = tk.Frame(self.root)
        self.cmdPanel.pack()

        self.start = tk.Button(self.cmdPanel, text="Start", command=self.run)
        self.start.pack()

        self.stopButton = tk.Button(
            self.cmdPanel, text="Stop", command=self.stop)
        self.stopButton.pack()

        self.resetButton = tk.Button(
            self.cmdPanel, text="Reset", command=self.reset)
        self.resetButton.pack()

        self.speedLabel = tk.Label(self.cmdPanel, text="Speed")
        self.speedLabel.pack()
        self.slider = tk.Scale(self.cmdPanel, from_=1,
                               to=30, orient="horizontal")
        self.slider.pack()

        self.isRunning = False

    def _run(self):
        self.isRunning = True
        row = 0
        for A, B in zip(self.gui, self.game.board):
            column = 0
            for a, b in zip(A, B):
                if a.state == b:
                    pass
                else:
                    self.game.board[row][column] = a.state
                column += 1
            row += 1
        # self.game.show()

        while self.isRunning:
            self.game.update()
            for A, B in zip(self.gui, self.game.board):
                for a, b in zip(A, B):
                    if a.state == b:
                        pass
                    else:
                        a.onClick()
            # self.game.show()
            self.root.update_idletasks()
            sleep(1/self.slider.get())

    def run(self):
        if not self.isRunning:
            thread = Thread(target=self._run)
            thread.start()

    def stop(self):
        self.isRunning = False

    def reset(self):
        self.isRunning = False
        row = 0
        for A, B in zip(self.gui, self.game.board):
            column = 0
            for a, b in zip(A, B):
                if a.state:
                    a.onClick()
                self.game.board[row][column] = 0
                column += 1
            row += 1

    def centerWindow(self):
        width = 500
        height = 600

        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def makeGrid(self, root):
        Tiles = []
        for row in range(self.game.rows):
            tiles = []
            for column in range(self.game.columns):
                tile = Tile(root)
                tile.button.grid(row=row, column=column)
                tiles.append(tile)
            Tiles.append(tiles)
        return Tiles

    def mainloop(self):
        self.root.mainloop()


# Main
if __name__ == "__main__":
    # TODO - auto adjust window size
    app = App()
    app.mainloop()
