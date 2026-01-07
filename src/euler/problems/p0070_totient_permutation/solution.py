"""
Problem 70: Totient Permutation
"""

from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


def is_permutation(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))


@timeit
def solve():
    """
    Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n
    and n/phi(n) is a minimum.
    """
    # Strategy:
    # 1. We want n/phi(n) to be minimized.
    #    n/phi(n) = product(p / (p-1)) for p|n.
    #    To minimize this, we want primes p to be as large as possible.
    # 2. n cannot be prime (phi(n)=n-1 is never a permutation of n).
    # 3. Best candidate is n = p1 * p2 where p1, p2 are large primes close to sqrt(10^7).
    #    sqrt(10^7) approx 3162.

    limit = 10**7

    # Generate primes in a safe range around sqrt(limit).
    # [2000, 5000] covers products up to 10^7 and ratios close to 1.
    primes = sieve_of_eratosthenes(5000)
    primes = [p for p in primes if p > 2000]

    min_ratio = float("inf")
    result_n = 0

    for i in range(len(primes)):
        p1 = primes[i]
        for j in range(i, len(primes)):
            p2 = primes[j]
            n = p1 * p2

            if n > limit:
                break

            # phi(n) = (p1-1)*(p2-1)
            phi = (p1 - 1) * (p2 - 1)

            if is_permutation(n, phi):
                ratio = n / phi
                if ratio < min_ratio:
                    min_ratio = ratio
                    result_n = n

    return result_n


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
