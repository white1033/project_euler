'''
Problem 6: Sum Square Difference
'''
from euler.utils.common import timeit


@timeit
def solve():
    """
    Calculates the difference using closed-form formulas (O(1)).
    """
    n = 100
    
    # Formula for 1 + 2 + ... + n
    sum_n = n * (n + 1) // 2
    square_of_sum = sum_n * sum_n
    
    # Formula for 1^2 + 2^2 + ... + n^2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    return square_of_sum - sum_of_squares

@timeit
def solve_brute_force():
    """
    Calculates the difference using iteration (O(n)).
    """
    n = 100
    sum_of_squares = sum(i * i for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print("--- Math Formula Approach ---")
    result = solve()
    print(f"Result: {result}")
    
    print("\n--- Brute Force Verification ---")
    verification = solve_brute_force()
    print(f"Verification: {verification}")
    
    assert result == verification