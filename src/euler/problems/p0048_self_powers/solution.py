"""
Problem 48: Self powers
"""

from euler.utils.common import timeit


@timeit
def solve():
    """
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    modulus = 10_000_000_000
    total_sum = 0
    
    for i in range(1, 1001):
        # Python's pow(base, exp, mod) is efficient modular exponentiation
        total_sum = (total_sum + pow(i, i, modulus)) % modulus
        
    return total_sum


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")