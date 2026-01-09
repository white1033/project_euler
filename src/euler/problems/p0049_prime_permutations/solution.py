"""
Problem 49: Prime Permutations
"""

from collections import defaultdict

from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


@timeit
def solve():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.
    What 12-digit number do you form by concatenating the three terms in this sequence?
    """
    # 1. Get all 4-digit primes
    primes = sieve_of_eratosthenes(9999)
    primes = [p for p in primes if p >= 1000]

    # 2. Group by fingerprint (sorted digits)
    groups = defaultdict(list)
    for p in primes:
        fingerprint = "".join(sorted(str(p)))
        groups[fingerprint].append(p)

    # 3. Check each group for arithmetic progression of length 3
    for _fingerprint, prime_list in groups.items():
        if len(prime_list) < 3:
            continue

        # The list is already sorted because we processed primes in order from sieve
        # prime_list.sort()

        n = len(prime_list)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = prime_list[i]
                p2 = prime_list[j]
                diff = p2 - p1
                p3 = p2 + diff

                # Check if p3 is in the list
                if p3 in prime_list:
                    # Found a sequence!
                    # Exclude the example given in the problem
                    if p1 == 1487 and p2 == 4817 and p3 == 8147:
                        continue

                    return f"{p1}{p2}{p3}"

    return None


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
