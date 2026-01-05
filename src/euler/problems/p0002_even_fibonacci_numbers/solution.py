'''
Problem 2: Even Fibonacci Numbers
'''
from euler.utils.common import timeit


@timeit
def solve():
    """
    Method 2: Optimal approach using E_n = 4*E_{n-1} + E_{n-2}
    Only generates even Fibonacci numbers.
    """
    limit = 4_000_000
    
    # Initialize first two even Fibonacci numbers: 2 and 8
    e1, e2 = 2, 8
    total_sum = e1
    
    while e2 <= limit:
        total_sum += e2
        # Next even number is 4 times current + previous
        e1, e2 = e2, 4 * e2 + e1
        
    return total_sum

@timeit
def solve_brute_force():
    """
    Method 1: Standard Fibonacci generation + Even check
    """
    limit = 4_000_000
    a, b = 1, 2
    total_sum = 0
    
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
        
    return total_sum

if __name__ == "__main__":
    print("--- Optimized Approach ---")
    result = solve()
    print(f"Result: {result}")
    
    print("\n--- Brute Force Verification ---")
    verification = solve_brute_force()
    print(f"Verification: {verification}")
    
    assert result == verification