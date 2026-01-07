"""
Problem 74: Digit Factorial Chains
"""

from euler.utils.common import timeit

FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def next_number(n: int) -> int:
    """Calculates the sum of the factorials of the digits of n."""
    s = 0
    temp = n
    if temp == 0:
        return FACTORIALS[0]
    while temp > 0:
        s += FACTORIALS[temp % 10]
        temp //= 10
    return s


@timeit
def solve(limit: int = 1000000) -> int:
    """
    How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
    """
    cache: dict[int, int] = {}
    count = 0

    for i in range(1, limit):
        curr = i
        path: list[int] = []

        # Traverse until we hit cache or a cycle in current path
        while curr not in cache:
            if curr in path:
                # Cycle detected within current path
                cycle_start_index = path.index(curr)
                cycle_len = len(path) - cycle_start_index

                # Update cache for all nodes in path
                for idx, node in enumerate(path):
                    if idx < cycle_start_index:
                        # Nodes before cycle: distance to cycle + cycle length
                        cache[node] = (cycle_start_index - idx) + cycle_len
                    else:
                        # Nodes in cycle: cycle length
                        cache[node] = cycle_len
                break

            path.append(curr)
            curr = next_number(curr)

        else:
            # We hit the cache (curr is in cache)
            remainder = cache[curr]
            # Update cache for everything in path
            for idx, node in enumerate(path):
                cache[node] = (len(path) - idx) + remainder

        if cache[i] == 60:
            count += 1

    return count


if __name__ == "__main__":
    print(solve())
