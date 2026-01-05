'''
Problem 34: Digit Factorials
'''
import math

from euler.utils.common import timeit


@timeit
def solve() -> int:
    """
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    # Precompute factorials for digits 0-9
    factorials = [math.factorial(d) for d in range(10)]
    
    # Determine upper bound
    # 9! = 362,880
    # 7 * 9! = 2,540,160 (7 digits)
    # 8 * 9! = 2,903,040 (7 digits, smaller than smallest 8-digit number 10,000,000)
    # So the upper bound is 2,540,160.
    upper_bound = 7 * factorials[9]
    
    total_sum = 0
    
    # Iterate from 3 (since 1! and 2! are excluded)
    for n in range(3, upper_bound + 1):
        # Calculate sum of digit factorials
        current_sum = 0
        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            current_sum += factorials[digit]
            temp_n //= 10
            
            # Optimization: If partial sum exceeds n, we can stop early?
            # Not necessarily, because n grows. But if current_sum > n_original, we can stop.
            # But we are modifying temp_n, so we need to compare with original n.
            if current_sum > n:
                break
        
        if current_sum == n:
            total_sum += n
            
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
