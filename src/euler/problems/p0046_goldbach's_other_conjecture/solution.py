"""
Problem 46: Goldbach's Other Conjecture
"""

import math
from euler.utils.common import timeit
from euler.utils.primes import is_prime


@timeit
def solve():
    """
    It was proposed by Christian Goldbach that every odd composite number can be written as 
    the sum of a prime and twice a square.
    9 = 7 + 2*1^2
    15 = 7 + 2*2^2
    ...
    Find the smallest odd composite that cannot be written as the sum of a prime and twice a square.
    """
    n = 9 # Start from the first odd composite
    
    while True:
        # Step 1: Check if n is composite
        if not is_prime(n):
            found_representation = False
            
            # Step 2: Try to find a prime p and square k^2 such that n = p + 2k^2
            # 2k^2 < n  =>  k^2 < n/2  =>  k < sqrt(n/2)
            limit_k = int(math.isqrt(n // 2))
            
            for k in range(1, limit_k + 1):
                remainder = n - 2 * (k * k)
                if is_prime(remainder):
                    found_representation = True
                    break
            
            # Step 3: If no representation found, this is the counter-example
            if not found_representation:
                return n
                
        # Move to next odd number
        n += 2

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")