import sys


def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # Check row
    for j in range(9):
        if grid[row][j] == num:
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check 3x3 box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False
    return True

def main():
    with open("sudoku.txt") as f:
        lines = f.readlines()

    total_sum = 0
    for i in range(0, len(lines), 10):
        # lines[i] is "Grid XX"
        grid = []
        for j in range(1, 10):
            grid.append([int(c) for c in lines[i+j].strip()])
        
        if solve_sudoku(grid):
            # The 3-digit number in the top left corner is grid[0][0], grid[0][1], grid[0][2]
            num = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
            total_sum += num
        else:
            print(f"Failed to solve {lines[i].strip()}")
            sys.exit(1)
            
    print(total_sum)

if __name__ == "__main__":
    main()
