"""
Problem 75: Singular Integer Right Triangles
"""

from math import gcd, isqrt

from euler.utils.common import timeit


@timeit
def solve(limit: int = 1500000) -> int:
    """
    Given that L is the length of the wire, for how many values of L <= limit can exactly
    one integer sided right angle triangle be formed?
    """
    counts = [0] * (limit + 1)

    # L = 2m(m+n)
    # m > n > 0, gcd(m, n) = 1, m, n opposite parity
    # 2m^2 < L <= limit => m < sqrt(limit/2)

    m_limit = isqrt(limit // 2)

    for m in range(2, m_limit + 1):
        for n in range(1, m):
            # Check conditions for primitive triples
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                perimeter = 2 * m * (m + n)

                if perimeter > limit:
                    break

                # Mark perimeter and its multiples
                for p in range(perimeter, limit + 1, perimeter):
                    counts[p] += 1

    # Count how many perimeters have exactly one solution
    result = 0
    for c in counts:
        if c == 1:
            result += 1

    return result


if __name__ == "__main__":
    print(solve())
