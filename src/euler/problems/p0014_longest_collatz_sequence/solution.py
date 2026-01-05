'''
Problem 14: Longest Collatz Sequence
'''
import sys
from functools import cache

from euler.utils.common import timeit

# Increase recursion depth just in case, though Collatz chains usually aren't *that* deep.
sys.setrecursionlimit(5000)

@cache
def get_chain_length(n: int) -> int:
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return 1 + get_chain_length(n // 2)
    else:
        return 1 + get_chain_length(3 * n + 1)

@timeit
def solve(limit: int = 1_000_000) -> int:
    """
    Which starting number, under one million, produces the longest chain?
    """
    max_length = 0
    max_starter = 0
    
    # Heuristic optimization: The longest chains are likely in the upper half.
    # We can iterate from limit//2 to limit, but iterating all is safe and fast enough.
    # Let's iterate all to be correct.
    # Optimization: We can skip n if we've already visited it as part of another chain?
    # With memoization, visiting is O(1).
    
    # We iterate range(1, limit). Note: "under one million" means < 1,000,000.
    for n in range(1, limit):
        length = get_chain_length(n)
        if length > max_length:
            max_length = length
            max_starter = n
            
    return max_starter

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
