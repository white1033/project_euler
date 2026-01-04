from euler.utils.common import timeit
from euler.utils.primes import is_prime

@timeit
def solve() -> int:
    """
    Finds the side length of the square spiral for which the ratio of primes
    along both diagonals first falls below 10%.
    """
    prime_count = 0
    total_count = 1  # Start with the center '1'
    s = 1
    
    while True:
        s += 2  # Expand to next layer
        
        # Calculate corners for side length s
        # Step size is s - 1
        # Corners are s^2, s^2 - (s-1), s^2 - 2(s-1), s^2 - 3(s-1)
        # We know s^2 is never prime.
        
        step = s - 1
        bottom_right = s * s
        
        # Check the other three corners
        c1 = bottom_right - step
        c2 = bottom_right - 2 * step
        c3 = bottom_right - 3 * step
        
        if is_prime(c1): prime_count += 1
        if is_prime(c2): prime_count += 1
        if is_prime(c3): prime_count += 1
        
        total_count += 4
        
        # Check ratio
        if prime_count / total_count < 0.10:
            return s

if __name__ == "__main__":
    print(solve())