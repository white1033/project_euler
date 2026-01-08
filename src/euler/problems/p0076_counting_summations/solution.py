"""
Problem 76: Counting Summations
"""

from euler.utils.common import timeit


@timeit
def solve_dp(n: int) -> int:
    """
    Solves using Dynamic Programming (Unbounded Knapsack style).
    Time Complexity: O(n^2)
    """
    # ways[i] will store the number of ways to partition integer i
    ways = [0] * (n + 1)
    ways[0] = 1

    # We can use integers from 1 up to n-1 (since we need at least two integers)
    # If we used 1 to n, we would get p(n) which includes n itself.
    # By using 1 to n-1, we naturally exclude the "n" case.
    for k in range(1, n):
        for j in range(k, n + 1):
            ways[j] += ways[j - k]

    return ways[n]


@timeit
def solve_pentagonal(n: int) -> int:
    """
    Solves using Euler's Pentagonal Number Theorem.
    p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k)
    where g_k = k(3k-1)/2

    Time Complexity: O(n * sqrt(n))
    """
    p = [0] * (n + 1)
    p[0] = 1

    for i in range(1, n + 1):
        k = 1
        while True:
            # Generalized pentagonal numbers for k and -k
            # k = 1, 2, 3... -> g_k = 1, 5, 12...
            # k = -1, -2, -3... -> g_k = 2, 7, 15...

            # Case 1: positive k
            g_k = (k * (3 * k - 1)) // 2
            if g_k > i:
                break

            sign = -1 if (k % 2 == 0) else 1
            p[i] += sign * p[i - g_k]

            # Case 2: negative k (let's use m = -k)
            # m = -k, so g_m = (-k)(-3k-1)/2 = k(3k+1)/2
            g_m = (k * (3 * k + 1)) // 2
            if g_m > i:
                break

            p[i] += sign * p[i - g_m]

            k += 1

    # The problem asks for partitions into at least two parts.
    # p[n] includes the partition 'n' itself (one part).
    # So we return p[n] - 1.
    return p[n] - 1


def solve(n: int = 100) -> int:
    # We'll run both to compare, but return one for the main interface
    print(f"Solving for n={n}...")
    res_dp = solve_dp(n)
    res_pent = solve_pentagonal(n)

    assert res_dp == res_pent, f"Mismatch! DP: {res_dp}, Pentagonal: {res_pent}"
    return res_dp


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
