"""
Problem 78: Coin Partitions
"""

from euler.utils.common import timeit


def _solve_iterative(
    target_n: int | None = None, divisor: int | None = None, modulus: int = 1000000
) -> int:
    """
    Internal solver.
    If target_n is set, returns p(target_n).
    If divisor is set, finds least n such that p(n) % divisor == 0.
    """
    p = [1]
    n = 1

    while True:
        # Check if we reached the target n
        if target_n is not None and len(p) > target_n:
            return p[target_n]

        current_p = 0
        k = 1
        while True:
            # Euler's Pentagonal Number Theorem:
            # p(n) = sum_{k!=0} (-1)^(k-1) * p(n - g_k)
            # Terms come in pairs: k=1, -1; k=2, -2; ...
            # Grouping pairs by |k|:
            # |k|=1 (1, -1) -> sign +
            # |k|=2 (2, -2) -> sign -
            # |k|=3 (3, -3) -> sign +
            # Sign pattern is +, -, +, -, ... corresponding to odd/even |k|

            # Case 1: Positive k
            g_k = (k * (3 * k - 1)) // 2

            if g_k > n:
                break

            sign = 1 if (k % 2 != 0) else -1

            val = p[n - g_k]
            if modulus:
                current_p = (current_p + sign * val) % modulus
            else:
                current_p += sign * val

            # Case 2: Negative k
            # Let m = -k. g_m = m(3m-1)/2 = -k(-3k-1)/2 = k(3k+1)/2
            g_k_neg = (k * (3 * k + 1)) // 2

            if g_k_neg > n:
                break

            val = p[n - g_k_neg]
            if modulus:
                current_p = (current_p + sign * val) % modulus
            else:
                current_p += sign * val

            k += 1

        # Ensure positive result if modulus is used (Python % usually handles this but to be safe)
        if modulus:
            current_p = (current_p + modulus) % modulus

        p.append(current_p)

        # Check divisibility condition
        if divisor and current_p == 0:
            return n

        n += 1


@timeit
def solve(divisor: int = 1000000) -> int:
    """
    Finds the least value of n for which p(n) is divisible by divisor.
    """
    # We use modulus = divisor because we only care about divisibility by divisor.
    # This prevents numbers from growing too large.
    return _solve_iterative(divisor=divisor, modulus=divisor)


def partition(n: int) -> int:
    """
    Helper to compute p(n) full value.
    """
    return _solve_iterative(target_n=n, modulus=0)


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
