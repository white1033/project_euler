'''
Problem 7: 10001st Prime
'''
from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes

@timeit
def solve(n: int = 10_001):
    """
    Finds the n-th prime number.
    
    We can use the Prime Number Theorem to estimate the magnitude of the nth prime.
    p_n ~ n * ln(n).
    
    A safe upper bound using p_n < n(ln n + ln ln n) is used to size the sieve.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    
    # Estimate limit
    if n < 6:
        limit = 20 # Small n case
    else:
        # p_n < n(ln n + ln ln n)
        import math
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 100
    
    primes = sieve_of_eratosthenes(limit)
    
    # In case our estimate was tight or off for very small n, extend if needed
    # (Though for n >= 6 the bound is strict, and for n < 6 we handled it)
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)
        
    return primes[n - 1]

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
