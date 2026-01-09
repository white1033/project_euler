"""
Problem 21: Amicable Numbers
"""

from euler.utils.common import timeit
from euler.utils.primes import sum_proper_divisors


@timeit
def solve(limit: int = 10000) -> int:
    """
    Evaluate the sum of all the amicable numbers under limit.
    """
    amicable_sum = 0

    # We can optimize by calculating sum_divisors for all numbers up to limit first?
    # Or just calculate on the fly. Since limit is 10000, on the fly is fine.
    # But wait, we need to handle the case where b > limit.
    # The problem asks for "sum of all amicable numbers under 10000".
    # This implies if a < 10000 and it has a pair b (even if b > 10000), a should be counted?
    # Re-reading: "Evaluate the sum of all the amicable numbers under 10000."
    # Usually this means if x is amicable and x < 10000, add x.
    # Even if its partner is > 10000.
    # However, for small limit like 10000, usually partners are close.
    # Let's iterate `a` < limit.

    for a in range(2, limit):
        b = sum_proper_divisors(a)
        if b > a and sum_proper_divisors(b) == a:
            amicable_sum += a
            # If b is also under limit, add it too.
            # If b >= limit, we don't add it because the question asks for numbers UNDER 10000.
            if b < limit:
                amicable_sum += b

    return amicable_sum


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
