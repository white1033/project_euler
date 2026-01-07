from math import gcd


def solve(limit: int = 12000) -> int:
    """
    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= limit?
    """
    count = 0

    # We iterate through all denominators d from 2 up to limit.
    # For each d, we want to find n such that:
    # 1/3 < n/d < 1/2
    # => d/3 < n < d/2

    for d in range(2, limit + 1):
        # lower_n calculation:
        # n > d/3. So smallest integer n is floor(d/3) + 1
        lower_n = d // 3 + 1

        # upper_n calculation:
        # n < d/2. So largest integer n is:
        # if d is even (d=2k), n < k => n <= k-1 => (d-1)//2
        # if d is odd (d=2k+1), n < k+0.5 => n <= k => (d-1)//2
        upper_n = (d - 1) // 2

        for n in range(lower_n, upper_n + 1):
            if gcd(n, d) == 1:
                count += 1

    return count
