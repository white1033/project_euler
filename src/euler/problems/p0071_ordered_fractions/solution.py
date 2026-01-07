def solve(limit: int = 1000000) -> int:
    """
    Finds the numerator of the fraction immediately to the left of 3/7
    for denominators <= limit.

    We want to find n/d < 3/7 such that n/d is maximized.
    This is equivalent to minimizing the difference 3/7 - n/d = (3d - 7n) / 7d.
    Since n, d are integers, the smallest positive value for 3d - 7n is 1.
    So we assume 3d - 7n = 1.

    This implies:
    3d ≡ 1 (mod 7)
    Multiply by 5 (modular inverse of 3 mod 7):
    15d ≡ 5 (mod 7)
    d ≡ 5 (mod 7)

    So d must be of the form 7k + 5.
    To minimize the difference 1/(7d), we must maximize d.
    """
    # Find the largest d <= limit such that d % 7 == 5
    # We can calculate this directly.
    # If limit % 7 >= 5, then floor(limit / 7) * 7 + 5 is the answer.
    # If limit % 7 < 5, then (floor(limit / 7) - 1) * 7 + 5 is the answer.
    # Alternatively, just iterate down from limit a few times.

    d = limit
    while d % 7 != 5:
        d -= 1

    n = (3 * d - 1) // 7

    return n
