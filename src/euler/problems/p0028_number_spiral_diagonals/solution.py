'''
Problem 28: Number Spiral Diagonals
'''
from euler.utils.common import timeit

@timeit
def solve(size: int = 1001) -> int:
    """
    What is the sum of the numbers on the diagonals in a size by size spiral formed in the same way?
    """
    if size % 2 == 0:
        raise ValueError("Size must be odd")
        
    total_sum = 1 # Center is always 1
    
    # Iterate through each layer (n x n square)
    # n starts from 3, goes up to size, increment by 2 (3, 5, 7, ...)
    for n in range(3, size + 1, 2):
        # The four corners of an n x n layer are:
        # Top Right: n^2
        # Top Left: n^2 - (n - 1)
        # Bottom Left: n^2 - 2(n - 1)
        # Bottom Right: n^2 - 3(n - 1)
        # Sum = 4n^2 - 6(n - 1) = 4n^2 - 6n + 6
        
        layer_sum = 4 * n * n - 6 * n + 6
        total_sum += layer_sum
        
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
