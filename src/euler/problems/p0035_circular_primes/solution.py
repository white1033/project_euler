"""
Problem 35: Circular Primes
"""

from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


def get_rotations(n: int) -> list[int]:
    """Generates all rotations of the number n."""
    s = str(n)
    rotations = []
    for _ in range(len(s)):
        s = s[1:] + s[0]
        rotations.append(int(s))
    return rotations


@timeit
def solve(limit: int = 1_000_000) -> int:
    """
    How many circular primes are there below limit?
    """
    primes = sieve_of_eratosthenes(limit - 1)
    primes_set = set(primes)

    circular_primes_count = 0

    # Digits that disqualify a multi-digit number from being a circular prime
    invalid_digits = {"0", "2", "4", "5", "6", "8"}

    for p in primes:
        s_p = str(p)

        # Optimization: Filter out primes with invalid digits if > 1 digit
        if len(s_p) > 1 and any(d in invalid_digits for d in s_p):
            continue

        # Check all rotations
        is_circular = True
        # Optimization: We can compute rotations using simple arithmetic or string slicing
        # String slicing is easier to read.

        # A number with d digits has d rotations.
        # We need to check if ALL rotations are in primes_set.

        # Note: get_rotations includes the number itself.
        for rot in get_rotations(p):
            if rot not in primes_set:
                is_circular = False
                break

        if is_circular:
            circular_primes_count += 1

    return circular_primes_count


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
