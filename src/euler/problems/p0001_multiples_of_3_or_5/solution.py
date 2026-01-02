'''
Problem 1: Multiples of 3 or 5
'''
from euler.utils.common import timeit

def sum_divisible_by(n: int, limit: int) -> int:
    """
    Calculates sum of multiples of n below limit.
    Example: sum_divisible_by(3, 10) -> 3 + 6 + 9 = 18
    """
    # Number of terms
    p = (limit - 1) // n
    # Sum of arithmetic series: n * (1 + 2 + ... + p)
    return n * (p * (p + 1)) // 2

@timeit
def solve():
    """
    O(1) solution using Inclusion-Exclusion Principle.
    """
    limit = 1000
    return sum_divisible_by(3, limit) + \
           sum_divisible_by(5, limit) - \
           sum_divisible_by(15, limit)

@timeit
def solve_brute_force():
    """
    O(N) iteration solution.
    """
    limit = 1000
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

if __name__ == "__main__":
    print("--- Math Approach ---")
    result = solve()
    print(f"Result: {result}")
    
    print("\n--- Brute Force Verification ---")
    verification = solve_brute_force()
    print(f"Verification: {verification}")
    
    assert result == verification