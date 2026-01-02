'''
Problem 5: Smallest Multiple
'''
import math
from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes

@timeit
def solve():
    """
    Calculates the smallest multiple of numbers 1 to 20 using prime factorization method.
    """
    limit = 20
    primes = sieve_of_eratosthenes(limit)
    result = 1
    
    for p in primes:
        # Find highest power of p that is <= limit
        # floor(log_p(limit)) gives the exponent
        if p * p > limit:
            # Optimization: If p^2 > limit, then p^1 is the highest power
            result *= p
        else:
            exponent = int(math.log(limit, p))
            result *= p ** exponent
            
    return result

@timeit
def solve_iterative():
    """
    Iterative LCM method for verification.
    """
    result = 1
    for i in range(2, 21):
        result = math.lcm(result, i)
    return result

if __name__ == "__main__":
    print("--- Prime Factorization Method ---")
    result = solve()
    print(f"Result: {result}")
    
    print("\n--- Iterative Verification ---")
    verification = solve_iterative()
    print(f"Verification: {verification}")
    
    assert result == verification