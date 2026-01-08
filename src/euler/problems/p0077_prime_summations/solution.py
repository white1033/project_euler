"""
Problem 77: Prime Summations
"""

from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


def compute_ways(limit: int) -> list[int]:
    """
    Computes the number of ways to write each number up to limit
    as a sum of primes.
    """
    primes = sieve_of_eratosthenes(limit)
    ways = [0] * (limit + 1)
    ways[0] = 1

    for p in primes:
        for j in range(p, limit + 1):
            ways[j] += ways[j - p]

    return ways


@timeit
def solve(threshold: int = 5000) -> int:
    """
    Finds the first value which can be written as the sum of primes
    in over `threshold` different ways.
    """
    limit = 10
    while True:
        ways = compute_ways(limit)
        # Search for the first number exceeding threshold
        for i in range(2, limit + 1):
            if ways[i] > threshold:
                return i

        # If not found, increase limit and retry
        limit *= 2


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
