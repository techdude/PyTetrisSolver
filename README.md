# PyTetrisSolver
A Tetris/Tetromino Solver Written in Python

This solver provides a generic engine for solving tetris style tiling problems where you
attempt to pack a certain number of oddly shaped tiles into a grid with a fixed number of
rows and columns. This can be done by rotating and placing the tiles.
When solved there are no empty spaces, although whole tiles 
may be left over (this solver assumes the number of tiles is the number available, however it
is simple to confirm using the solution list whether all tiles were needed or not). 

The solver can provide raw tabular output useful for those just curious in using in personally, 
and it can also provide a solution list which allows the solver to be used in other software,
and the solutions can be used programatically.

It is a generic solver which means that the solver comes with a set of common tetrominos, however
the programmer can easily specify other tile patterns for the solver to use (see the Custom Tile example).

## Examples

### Example 1: Basic Usage

```python
problem = TileSolver.TileSolver(
	boardRows = 6,
	boardCols = 8,
	tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.ZTile],
	numTiles = [2, 3, 2, 1, 2, 2]
)
if problem.solveProblem():
	print("Found solution: ")
	TileSolver.printMatrix(problem.solutionBoard)
else:
	print("No solution found")
```

Output:
![Output of Example](http://i.imgur.com/a0U3mal.png "Output of Example")

### Example 2: Custom Output

```python
customTiles = [TileSolver.LTile, TileSolver.SquareTile]
problem = TileSolver.TileSolver(
    boardRows = 4,
    boardCols = 6,
    tiles = customTiles,
    numTiles = [4, 2]
)
if problem.solveProblem():
    print("Found solution: ")
    for tilePlacement in problem.solution:
        print("Tile: %i" %(tilePlacement["tile"]))
        print("\tRow: %i" %(tilePlacement["row"]))
        print("\tColumn: %i" %(tilePlacement["col"]))
        print("\tRotation: %i" %(tilePlacement["rotation"]))
else:
    print("No solution found")
```

Output:
![Output of Example](http://i.imgur.com/14roQiL.png "Output of Example")

### Example 3: Custom Tile

To use custom tiles, you can simply extend the tile class, and override 
the tile property with the definition list, and override the uniqueRotations
with the number of rotations that produce unique shapes. The example is shown below.

Notice how you can declare any custom tile shape by griding it out in rows and columns.
The weights should be all 1 where there is a filled part of the tile, and 0 otherwise.
The tile should be written with the matrix as closely fitted as possible. It shouldn't
have any completely zero rows or columns.

```python
'''
    Define the weird tile. Due to its shape, there are 4 distinct rotational appearances of the tile.
'''
class WeirdTile(TileSolver.Tile):
    tile = [
        [0,1,0],
        [0,1,1],
        [0,1,1],
        [1,1,1]
    ]
    uniqueRotations = 4 #We could also omit this for the default of 4

problem = TileSolver.TileSolver(
    boardRows = 8,
    boardCols = 5,
    tiles = [TileSolver.LTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.ZTile, WeirdTile],
    numTiles = [2, 1, 2, 1, 2, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")
```

Output:
![Output of Example](http://i.imgur.com/RrluPCV.png "Output of Example")

