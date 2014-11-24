Life is a simple simulation of cell automata.

Life contains a two-dimensional grid of cells. A cell can only be in one of two states: alive or dead. There are two kinds of cells: ConwayCells and FredkinCells.

Once the grid is manually populated with live and/or dead cells, the grid represents the 0th generation of Life. After that, everything is automatic, and Life evolves from the 1st to the Nth generation. A generation is simply the state of the grid (i.e. the layout of the live and dead cells).

Live ConwayCells are denoted with an asterisk, "*", and dead cells are denoted with a period, ".". A ConwayCell has 8 neighbors, if it's an interior cell, 5 neighbors, if it's an edge cell, and 3 neighbors, if it's a corner cell. The example below is of 1 ConwayCell that is alive surrounded by 8 ConwayCells that are dead:

    ...
    .*.
    ...
ConwayCells do not have the notion of age, FredkinCells do. A FredkinCell's age is initially zero and only increments by one if the cell is alive and stays alive. Its age never goes down.

Live FredkinCells are denoted with their age, if their age is less than 10, otherwise denoted with a plus, "+", and dead cells are denoted with a minus, "-". A FredkinCell has 4 neighbors, if it's an interior cell, 3 neighbors, if it's an edge cell, and 2 neighbors, if it's a corner cell. The example below is of 1 FredkinCell that is alive and of age 5 surrounded by 4 FredkinCells that are dead:

      -
    - 5 -
      -
The rules for going from one generation to the next for ConwayCells are:

a dead cell becomes a live cell, if exactly 3 neighbors are alive
a live cell becomes a dead cell, if less than 2 or more than 3 neighbors are alive
The rules for going from one generation to the next for FredkinCells are:

a dead cell becomes a live cell, if 1 or 3 neighbors are alive
a live cell becomes a dead cell, if 0, 2, or 4 neighbors are alive
When a FredkinCell's age is to become 2, and only then, it becomes a live ConwayCell instead.


