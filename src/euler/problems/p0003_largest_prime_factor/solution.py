'''
Problem 3: Largest Prime Factor
'''
from euler.utils.common import timeit
from euler.utils.primes import get_prime_factors

@timeit
def solve():
    """
    Finds the largest prime factor of 600851475143.
    """
    target = 600851475143
    
    # We just need the last factor yielded by our generator
    last_factor = 0
    for factor in get_prime_factors(target):
        last_factor = factor
        
    return last_factor

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")