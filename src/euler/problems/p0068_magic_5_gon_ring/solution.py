"""
Problem 68: Magic 5-gon ring
"""

from itertools import permutations

from euler.utils.common import timeit


@timeit
def solve():
    """
    Find the maximum 16-digit string for a "magic" 5-gon ring.
    """
    # We need to fill 10 positions: 5 outer (O), 5 inner (I)
    # Positions in permutation p:
    # Outer: 0, 1, 2, 3, 4
    # Inner: 5, 6, 7, 8, 9
    #
    # Lines (O, I1, I2):
    # 0: p[0], p[5], p[6]
    # 1: p[1], p[6], p[7]
    # 2: p[2], p[7], p[8]
    # 3: p[3], p[8], p[9]
    # 4: p[4], p[9], p[5]

    max_string = ""
    # Optimization:
    # 1. 10 must be in Outer ring (to keep string 16 digits).
    # 2. Due to rotational symmetry, we can FIX 10 at the first Outer position (index 0).
    #    This reduces the search space from 10! (3.6M) to 9! (362k), a 10x speedup.

    # We fix p[0] = 10. We permute 1..9 for the remaining 9 slots.
    others = list(range(1, 10))

    for p_tail in permutations(others):
        p = (10,) + p_tail

        # Check sums
        # p[0] is 10. Outer nodes are p[0]..p[4].

        s0 = p[0] + p[5] + p[6]
        s1 = p[1] + p[6] + p[7]
        if s0 != s1:
            continue

        s2 = p[2] + p[7] + p[8]
        if s0 != s2:
            continue

        s3 = p[3] + p[8] + p[9]
        if s0 != s3:
            continue

        s4 = p[4] + p[9] + p[5]
        if s0 != s4:
            continue

        # If valid, construct the string
        # 1. Find the starting node (lowest outer node)
        outer_nodes = p[:5]
        min_outer = min(outer_nodes)
        start_idx = outer_nodes.index(min_outer)

        # 2. Build string starting from that index
        concat_str = ""
        for k in range(5):
            idx = (start_idx + k) % 5
            # Line: Outer, Inner1, Inner2
            n1 = p[idx]
            n2 = p[5 + idx]
            n3 = p[5 + (idx + 1) % 5]
            concat_str += f"{n1}{n2}{n3}"

        # 3. Check length and update max
        if len(concat_str) == 16 and concat_str > max_string:
            max_string = concat_str

    return int(max_string)


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
