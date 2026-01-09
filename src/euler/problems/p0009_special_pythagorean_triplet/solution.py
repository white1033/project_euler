"""
Problem 9: Special Pythagorean Triplet
"""

from euler.utils.common import timeit


@timeit
def solve(target_sum: int = 1000) -> int:
    """
    Finds the product abc of a Pythagorean triplet where a + b + c = target_sum.

    Optimized approach using Euclid's formula: O(sqrt(N)).
    a = k(m^2 - n^2), b = k(2mn), c = k(m^2 + n^2)
    a + b + c = 2km(m + n) = S
    => km(m + n) = S / 2

    Since n > 0, m(m+n) > m^2 => m < sqrt(S/2).
    We iterate m and look for valid k, n.
    """
    if target_sum % 2 != 0:
        return -1  # Sum of Pythagorean triplet is always even

    half_s = target_sum // 2
    limit_m = int(half_s**0.5)

    for m in range(2, limit_m + 1):
        if half_s % m == 0:
            # rest = k * (m + n)
            rest = half_s // m

            # We iterate k to find n.
            # Since m + n = rest / k and n < m < m+n < 2m
            # => rest / k < 2m => k > rest / (2m)
            # Also n > 0 => m+n > m => rest / k > m => k < rest / m

            # Iterate valid k ranges. Note that k must divide rest.
            # Optimization: iterate k directly? Or iterate n?
            # Iterating k is safer for finding factors.

            # rest = k * (m + n).
            # We derive bounds for k:
            # 1. n < m  =>  m + n < 2m  =>  rest / k < 2m  =>  k > rest / (2m)
            # 2. n > 0  =>  m + n > m   =>  rest / k > m   =>  k < rest / m

            lower_k = rest // (2 * m) + 1
            upper_k = (rest + m - 1) // m  # Ceiling divisionish, but k < rest/m strictly
            # Actually integer division `rest // m` is the upper bound inclusive if rest/m is integer,
            # but since n > 0, k cannot be exactly rest/m.
            # So range is valid.

            for k in range(lower_k, upper_k):  # k < rest/m
                if rest % k == 0:
                    m_plus_n = rest // k
                    n = m_plus_n - m
                    # Double check conditions (redundant given loop bounds but safe)
                    if 0 < n < m:
                        a = k * (m * m - n * n)
                        b = k * (2 * m * n)
                        c = k * (m * m + n * n)
                        return a * b * c

    return -1


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
