"""
Problem 50: Consecutive Prime Sum
"""

from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


@timeit
def solve():
    """
    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    The longest sum of consecutive primes below one-thousand that adds to a prime,
    contains 21 terms, and is equal to 953.
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    """
    limit = 1_000_000
    primes = sieve_of_eratosthenes(limit)
    primes_set = set(primes)

    max_length = 0
    result = 0

    # Prefix sums allows O(1) sum calculation for any range
    # prefix_sum[k] = sum of first k primes
    prefix_sum = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix_sum[i + 1] = prefix_sum[i] + primes[i]

    # We iterate length from max possible down to current max_length
    # Max possible length? Sum of first k primes < 1,000,000
    # We can estimate or just let the loop break naturally.
    # Actually, iterating start index 'i' and then extending length 'j' is easier to code logic-wise.
    # But for finding MAX length, iterating length from large to small allows early exit?
    # Not necessarily, because a smaller length might produce a valid prime sum (though we want max length).

    # Let's stick to the double loop: i (start index), j (length)
    # Optimization: The sum grows very fast.
    # The inner loop will break quickly.

    # Optimization 2: We can calculate the upper bound for length
    # sum(primes[:550]) is already > 1,000,000. So max length < 600.

    for i in range(len(primes)):
        # If the single prime itself is beyond limit (impossible here since sieve is limited), break
        # If the minimum sum starting at i with current max_length exceeds limit, we can stop?
        # Min sum of length L starting at i is roughly L * primes[i].
        # But let's just use the direct sum check.

        current_sum = 0
        for j in range(i, len(primes)):
            current_sum += primes[j]

            if current_sum >= limit:
                break

            length = j - i + 1
            if length > max_length and current_sum in primes_set:
                max_length = length
                result = current_sum

    return result


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
