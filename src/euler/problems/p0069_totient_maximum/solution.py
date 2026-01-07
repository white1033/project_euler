"""
Problem 69: Totient Maximum
"""

from euler.utils.common import timeit
from euler.utils.primes import is_prime


@timeit
def solve(limit: int = 1000000) -> int:
    """
    Find the value of n <= limit for which n/phi(n) is a maximum.
    """
    # Analysis shows that n/phi(n) is maximized when n is a product of consecutive small primes.
    # n/phi(n) = product(p / (p-1)) for p|n.
    # This product is maximized when we include as many small primes as possible.

    result = 1
    current_prime = 2

    while True:
        if is_prime(current_prime):
            if result * current_prime > limit:
                break
            result *= current_prime
        current_prime += 1

    return result


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
