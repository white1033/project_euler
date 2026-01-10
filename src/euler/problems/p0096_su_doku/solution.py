import os

from euler.utils.common import timeit


def solve_sudoku(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(grid, r, c, n):
                        grid[r][c] = n
                        if solve_sudoku(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True


def is_valid(grid, r, c, n):
    if n in grid[r]:
        return False

    for i in range(9):
        if grid[i][c] == n:
            return False

    br, bc = 3 * (r // 3), 3 * (c // 3)
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == n:
                return False
    return True


@timeit
def solve() -> int:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "sudoku.txt")

    grids = []
    with open(file_path) as f:
        lines = f.readlines()

    current_grid = []
    for line in lines:
        if "Grid" in line:
            if current_grid:
                grids.append(current_grid)
            current_grid = []
        else:
            row = [int(c) for c in line.strip()]
            current_grid.append(row)
    if current_grid:
        grids.append(current_grid)

    total = 0
    for grid in grids:
        solve_sudoku(grid)
        val = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
        total += val

    return total


if __name__ == "__main__":
    print(solve())
