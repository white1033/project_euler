import math
from typing import Generator, List

def get_prime_factors(n: int) -> Generator[int, None, None]:
    """
    Generates prime factors of n in ascending order.
    Example: get_prime_factors(12) -> 2, 2, 3
    """
    # Handle 2 separately to allow stepping by 2 later
    while n % 2 == 0:
        yield 2
        n //= 2
    
    # Try odd numbers from 3 up to sqrt(n)
    d = 3
    while d * d <= n:
        while n % d == 0:
            yield d
            n //= d
        d += 2
        
    # If n > 1, the remaining n is a prime
    if n > 1:
        yield n

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Returns a list of all primes <= limit.
    """
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(math.isqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
                
    return [num for num, is_prime in enumerate(sieve) if is_prime]