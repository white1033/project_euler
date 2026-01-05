'''
Problem 30: Digit Fifth Powers
'''
from euler.utils.common import timeit


@timeit
def solve(power: int = 5) -> int:
    """
    Find the sum of all the numbers that can be written as the sum of `power` powers of their digits.
    """
    # Precompute powers of digits 0-9
    digit_powers = [d**power for d in range(10)]
    
    # Determine upper bound
    # n * 9^power must have n digits
    # For power=5, 6 * 9^5 = 354294 (6 digits), 7 * 9^5 = 413343 (6 digits)
    # So 7 digits is impossible. Max bound is roughly 6 * 9^5.
    upper_bound = 6 * (9**power)
    
    total_sum = 0
    
    # Iterate from 2 to upper bound (1 is excluded by definition)
    for n in range(2, upper_bound + 1):
        # Calculate sum of powers of digits
        # This can be optimized by not converting to string every time, but str is fast enough in Python
        current_sum = sum(digit_powers[int(d)] for d in str(n))
        
        if current_sum == n:
            total_sum += n
            
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
