# Conway-s-Game-of-Life

Rules:

-   Any live cell with fewer than two live neighbors dies, as if caused by under population.
-   Any live cell with two or three live neighbors lives on to the next generation.
-   Any live cell with more than three live neighbors dies, as if by overpopulation.
-   Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Prerequisites

### Ubuntu

`sudo apt-get install python3-tk`

### Windows

Python 3.6 and above

## Instructions:

Just run the `main.py` and a window should pop up with a clickable 9x9 grid.

## Troubleshooting

If the grid aspect ratio isn't 1:1, change the line
`self.button.configure(heigh=2, width=4)`
in the  `__init__` method of the `Tile` class to
`self.button.configure(heigh=2, width=2)`. 

If you can't fully see the grid and the buttons, change the `width` and `height` in the `App` method `centerWindow`.
