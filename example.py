'''
    Example usage of Tile Solver
'''

import TileSolver

#Example 1: Full example with error handling and table output
print("====================Example 1=====================")
problem = TileSolver.TileSolver(
    boardRows = 6,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.SquareTile, TileSolver.STile],
    numTiles = [4, 1, 4]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")

#Example 2: Custom solution output handling
customTiles = [TileSolver.LTile, TileSolver.SquareTile];
print("====================Example 2=====================")
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

#Examples 3 and up: Additional example puzzles
print("====================Example 3=====================")
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


print("====================Example 4=====================")
problem = TileSolver.TileSolver(
    boardRows = 6,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.ZTile],
    numTiles = [2, 2, 1, 2, 2]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 5=====================")
problem = TileSolver.TileSolver(
    boardRows = 10,
    boardCols = 4,
    tiles = [TileSolver.LTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.STile],
    numTiles = [2, 4, 1, 2, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 6=====================")
problem = TileSolver.TileSolver(
    boardRows = 6,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.ZTile],
    numTiles = [2, 2, 2, 3]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 7=====================")
problem = TileSolver.TileSolver(
    boardRows = 6,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.STile],
    numTiles = [2, 1, 2, 1, 2, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 8=====================")
problem = TileSolver.TileSolver(
    boardRows = 8,
    boardCols = 5,
    tiles = [TileSolver.LTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.ZTile, TileSolver.STile],
    numTiles = [2, 2, 2, 1, 2, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 9=====================")
problem = TileSolver.TileSolver(
    boardRows = 8,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.SquareTile, TileSolver.ZTile, TileSolver.STile],
    numTiles = [1, 1, 4, 2, 2, 2]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")

print("====================Example 10=====================")
problem = TileSolver.TileSolver(
    boardRows = 7,
    boardCols = 8,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile, TileSolver.ZTile, TileSolver.STile],
    numTiles = [1, 1, 4, 2, 4, 1, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 11=====================")
problem = TileSolver.TileSolver(
    boardRows = 5,
    boardCols = 8,
    tiles = [TileSolver.LTile, TileSolver.ReverseLTile, TileSolver.TTile, TileSolver.LineTile, TileSolver.SquareTile],
    numTiles = [2, 1, 4, 2, 1]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")


print("====================Example 12=====================")
problem = TileSolver.TileSolver(
    boardRows = 6,
    boardCols = 6,
    tiles = [TileSolver.LTile, TileSolver.SquareTile, TileSolver.STile],
    numTiles = [4, 1, 4]
)
if problem.solveProblem():
    print("Found solution: ")
    TileSolver.printMatrix(problem.solutionBoard)
else:
    print("No solution found")
