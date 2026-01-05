'''
Problem 23: Non-Abundant Sums
'''
from euler.utils.common import timeit
from euler.utils.primes import sum_proper_divisors


@timeit
def solve(limit: int = 28123) -> int:
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    The problem states that all integers greater than 28123 can be written as the sum of two abundant numbers.
    """
    # 1. Find all abundant numbers up to the limit
    abundants = []
    for i in range(12, limit + 1): # 12 is the smallest abundant number
        if sum_proper_divisors(i) > i:
            abundants.append(i)
            
    # 2. Mark all sums of two abundant numbers
    can_be_written = [False] * (limit + 1)
    
    # Iterate through all pairs of abundant numbers
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s > limit:
                break
            can_be_written[s] = True
            
    # 3. Sum numbers that cannot be written
    total_sum = sum(i for i in range(1, limit + 1) if not can_be_written[i])
    
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
