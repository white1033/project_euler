from pathlib import Path

from euler.utils.common import timeit


@timeit
def solve():
    current_dir = Path(__file__).parent

    matrix_path = current_dir / "0081_matrix.txt"

    if not matrix_path.exists():
        matrix_path = current_dir / "matrix.txt"
        if not matrix_path.exists():
            raise FileNotFoundError(f"Could not find matrix file at {current_dir}")

    with open(matrix_path) as f:
        matrix = [[int(num) for num in line.strip().split(",")] for line in f if line.strip()]

    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(1, cols):
        matrix[0][j] += matrix[0][j - 1]

    for i in range(1, rows):
        matrix[i][0] += matrix[i - 1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[rows - 1][cols - 1]


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
