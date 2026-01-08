"""
Problem 80: Square Root Digital Expansion
"""

import math

from euler.utils.common import timeit


def calculate_digital_sum(n: int, precision: int = 100) -> int:
    """
    Calculates the sum of the first `precision` digits of sqrt(n).
    Uses high-precision integer arithmetic.
    """
    # To get 'precision' digits of sqrt(n), we compute integer sqrt of n * 10^(2*P).
    # We add a buffer to P (e.g., +10) to ensure stability of the last required digits.
    # sqrt(n * 10^(2*k)) = sqrt(n) * 10^k
    # This shifts the decimal point k places to the right.

    shift = 10 ** (2 * (precision + 10))
    val = n * shift
    root = math.isqrt(val)

    s = str(root)
    # The result string contains the first significant digits.
    # Since 1 <= n < 100, sqrt(n) is between 1 and 9.99...
    # So the first digit corresponds to the integer part (1-9).
    # We simply take the first `precision` characters.
    digits = s[:precision]

    return sum(int(d) for d in digits)


@timeit
def solve(limit: int = 100) -> int:
    """
    Finds the total of the digital sums of the first 100 decimal digits
    for all the irrational square roots for the first `limit` natural numbers.
    """
    total_sum = 0
    for n in range(1, limit + 1):
        # Skip perfect squares
        # math.isqrt returns the integer part of the square root.
        root = math.isqrt(n)
        if root * root == n:
            continue

        total_sum += calculate_digital_sum(n, 100)

    return total_sum


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
