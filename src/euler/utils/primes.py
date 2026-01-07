import math
from collections.abc import Generator


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime using the Miller-Rabin primality test.
    This is deterministic for n < 3,317,044,064,279,371 using the selected bases.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # For small numbers, Trial Division is still very fast and has less overhead
    if n < 1000:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # Miller-Rabin Primality Test
    # Write n-1 as 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness bases deterministic for n < 4,759,123,141
    # For larger n (up to 2^64), we would need more bases: [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    # Since Project Euler problems rarely exceed 2^64, we can expand the bases if needed.
    # For this specific problem (n ~ 7*10^8), [2, 7, 61] is sufficient.
    # To be safe for general use up to 2^64, we use the larger set.

    if n < 4759123141:
        bases = [2, 7, 61]
    else:
        bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    for a in bases:
        if a >= n:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


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


def sum_proper_divisors(n: int) -> int:
    """
    Returns the sum of proper divisors of n (divisors less than n).
    Example: 12 -> 1 + 2 + 3 + 4 + 6 = 16
    """
    if n <= 1:
        return 0

    sum_divs = 1
    exponents: dict[int, int] = {}
    for factor in get_prime_factors(n):
        exponents[factor] = exponents.get(factor, 0) + 1

    for p, e in exponents.items():
        # Sum of powers of p: 1 + p + ... + p^e = (p^(e+1) - 1) // (p - 1)
        sum_divs *= (p ** (e + 1) - 1) // (p - 1)

    return sum_divs - n


def count_divisors(n: int) -> int:
    """
    Calculates the number of divisors of n using prime factorization.
    If n = p1^a * p2^b * ..., divisors = (a+1) * (b+1) * ...
    """
    if n == 1:
        return 1

    exponents: dict[int, int] = {}
    for factor in get_prime_factors(n):
        exponents[factor] = exponents.get(factor, 0) + 1

    count = 1
    for exp in exponents.values():
        count *= exp + 1

    return count


def sieve_of_eratosthenes(limit: int) -> list[int]:
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


def sieve_totient(limit: int) -> list[int]:
    """
    Computes Euler's Totient Function phi(n) for all n <= limit using a sieve.
    Returns a list where list[i] = phi(i).
    """
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    return phi
