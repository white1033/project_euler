import math


def solve() -> int:
    """
    Calculates how many n-digit positive integers exist which are also an nth power.

    We are looking for integers x such that x = a^n and x has exactly n digits.
    This condition implies:
    10^(n-1) <= a^n < 10^n

    Taking log10:
    n - 1 <= n * log10(a) < n

    From the right inequality:
    n * log10(a) < n  => log10(a) < 1 => a < 10.
    So a can be 1, 2, ..., 9.

    From the left inequality:
    n - 1 <= n * log10(a)
    n - n * log10(a) <= 1
    n * (1 - log10(a)) <= 1
    n <= 1 / (1 - log10(a))

    For each a in [1, 9], the number of valid n values is floor(1 / (1 - log10(a))).
    Since n must be at least 1, and the lower bound 10^(n-1) <= a^n is what limits n,
    we just sum these counts for each a.
    """
    count = 0
    for a in range(1, 10):
        limit = int(1 / (1 - math.log10(a)))
        count += limit
    
    return count