# Su Doku

## Problem 96

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward logic.

The 6K text file, [sudoku.txt](https://projecteuler.net/project/resources/p096_sudoku.txt), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

## Analysis

This problem requires a programmatic Sudoku solver. Since the grid size is fixed at $9 \times 9$ and there are only 50 puzzles, a simple recursive backtracking algorithm is sufficient.

### Algorithm (Backtracking)
1. Find the first empty cell (containing 0).
2. If no empty cells exist, the puzzle is solved.
3. Try placing digits 1 through 9 in the empty cell.
4. For each digit, check if it's valid (not present in current row, column, or $3 \times 3$ box).
5. If valid, place the digit and recursively attempt to solve the rest of the grid.
6. If the recursive call returns true, the solution is found.
7. If the recursive call returns false (backtrack), reset the cell to 0 and try the next digit.
8. If no digit leads to a solution, return false.

### Optimization
While finding the "most constrained" cell (fewest possible candidates) significantly speeds up solving hard puzzles, finding the *first* empty cell is simpler to implement and fast enough for this set of puzzles (Project Euler problems typically execute in < 1 second).

### Verification
We solve each of the 50 grids and extract the number formed by the first three digits of the first row: $100 \times \text{grid}[0][0] + 10 \times \text{grid}[0][1] + \text{grid}[0][2]$. We sum these values for the final answer.
