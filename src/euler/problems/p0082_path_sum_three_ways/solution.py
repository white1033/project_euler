from pathlib import Path

from euler.utils.common import timeit


@timeit
def solve():
    current_dir = Path(__file__).parent

    possible_files = ["0082_matrix.txt", "matrix.txt"]
    matrix_path = None

    for fname in possible_files:
        p = current_dir / fname
        if p.exists():
            matrix_path = p
            break

    if not matrix_path:
        raise FileNotFoundError(f"Could not find matrix file in {current_dir}")

    with open(matrix_path) as f:
        matrix = [[int(num) for num in line.strip().split(",")] for line in f if line.strip()]

    rows = len(matrix)
    cols = len(matrix[0])

    min_path = [matrix[i][0] for i in range(rows)]

    for j in range(1, cols):
        current_col_cost = [min_path[i] + matrix[i][j] for i in range(rows)]

        for i in range(1, rows):
            current_col_cost[i] = min(current_col_cost[i], current_col_cost[i - 1] + matrix[i][j])

        for i in range(rows - 2, -1, -1):
            current_col_cost[i] = min(current_col_cost[i], current_col_cost[i + 1] + matrix[i][j])

        min_path = current_col_cost

    return min(min_path)


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
