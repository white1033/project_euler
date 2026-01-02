'''
Problem 10: Summation of Primes
'''
from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes

@timeit
def solve(limit: int = 2_000_000) -> int:
    """
    Finds the sum of all the primes below the given limit.
    """
    # The problem asks for primes BELOW 2 million, so strictly less than limit.
    # sieve_of_eratosthenes(n) typically returns primes <= n.
    # If we pass limit - 1, we get primes <= limit - 1, which is effectively < limit.
    primes = sieve_of_eratosthenes(limit - 1)
    return sum(primes)

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
