"""
Problem 37: Truncatable Primes
"""

from euler.utils.common import timeit
from euler.utils.primes import is_prime


def is_left_truncatable(n: int) -> bool:
    """
    Check if a number is left-truncatable prime.
    Example: 3797 -> 797 -> 97 -> 7 (all must be prime)
    """
    s = str(n)
    # We start from index 1 because the number itself is already checked
    # (it is passed in as a known prime or checked before calling this).
    # But for safety, let's assume we need to check sub-parts.
    # The problem implies the number itself must be prime, which our generator ensures.
    # So we check s[1:], s[2:], ...
    return all(is_prime(int(s[i:])) for i in range(1, len(s)))


@timeit
def solve():
    """
    Find the sum of the only eleven primes that are both truncatable from left to right
    and right to left.
    """
    # 2, 3, 5, 7 are not considered truncatable primes (per problem note).
    # However, they are the roots of our Right-Truncatable search tree.

    # Queue for BFS: stores Right-Truncatable Primes
    queue = [2, 3, 5, 7]

    truncatable_primes = []

    # Digits we can append.
    # We cannot append 0, 2, 4, 6, 8, 5 because the resulting number
    # (which is > 1 digit) would be divisible by 2 or 5.
    valid_extensions = [1, 3, 7, 9]

    while queue:
        current_prime = queue.pop(0)

        for digit in valid_extensions:
            next_num = current_prime * 10 + digit

            if is_prime(next_num):
                # It is Right-Truncatable (since parent was, and this new one is prime)
                queue.append(next_num)

                # Check if it is also Left-Truncatable
                # Note: Single digit primes are excluded by problem statement,
                # but our generator creates >1 digit numbers here.
                if is_left_truncatable(next_num):
                    truncatable_primes.append(next_num)

    # Just a sanity check, the problem says there are 11.
    # print(f"Found {len(truncatable_primes)} truncatable primes: {truncatable_primes}")

    return sum(truncatable_primes)


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
