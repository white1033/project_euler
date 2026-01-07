"""
Problem 67: Maximum Path Sum II
"""

from pathlib import Path
from euler.utils.common import timeit


@timeit
def solve():
    """
    Finds the maximum total from top to bottom of the triangle.
    Uses bottom-up dynamic programming.
    """
    # Read the triangle from the file
    current_dir = Path(__file__).parent
    with open(current_dir / "triangle.txt", "r") as f:
        triangle_str = f.read()

    triangle = [[int(num) for num in line.split()] for line in triangle_str.strip().split("\n")]

    # Start from the second to last row and move upwards
    # len(triangle) - 2 is the index of the second to last row
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            # Update current cell with itself + max of the two children
            triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])

    # The top element now contains the maximum path sum
    return triangle[0][0]


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
