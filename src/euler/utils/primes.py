import math
from typing import Generator

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
