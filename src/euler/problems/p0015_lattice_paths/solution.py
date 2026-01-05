'''
Problem 15: Lattice Paths
'''
import math

from euler.utils.common import timeit


@timeit
def solve(grid_size: int = 20) -> int:
    """
    How many such routes are there through a grid_size x grid_size grid?
    
    Total steps = 2 * grid_size (grid_size Right, grid_size Down).
    We need to choose `grid_size` steps to be Right (or Down).
    Result is C(2*n, n).
    """
    n = grid_size
    return math.comb(2 * n, n)

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
