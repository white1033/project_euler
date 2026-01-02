'''
Problem 0: Sum of odd squares
'''
from euler.utils.common import timeit

def sum_squares(n: int) -> int:
    """Calculates sum of 1^2 + ... + n^2 using formula."""
    return n * (n + 1) * (2 * n + 1) // 6

@timeit
def solve():
    """
    Calculates sum of odd squares up to N=491,000 using closed-form formula.
    Logic: Sum(Odd) = Sum(All) - Sum(Even)
    """
    N = 491000
    
    # 1. Sum of all squares from 1^2 to N^2
    total_sum = sum_squares(N)
    
    # 2. Sum of even squares: (2^2 + 4^2 + ... + (2m)^2) = 4 * (1^2 + ... + m^2)
    m = N // 2
    even_sum = 4 * sum_squares(m)
    
    return total_sum - even_sum

@timeit
def solve_brute_force():
    """
    Verification using simple iteration.
    """
    N = 491000
    # Sum k^2 for odd k in range [1, N]
    # range(1, N + 1, 2) generates 1, 3, 5, ...
    return sum(k * k for k in range(1, N + 1, 2))

if __name__ == "__main__":
    print("--- Math Approach ---")
    result = solve()
    print(f"Result: {result}")
    
    print("\n--- Brute Force Verification ---")
    verification = solve_brute_force()
    print(f"Verification: {verification}")
    
    assert result == verification