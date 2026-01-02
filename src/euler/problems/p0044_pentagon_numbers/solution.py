"""
Problem 44: Pentagon Numbers
"""

import math
from euler.utils.common import timeit


def is_pentagonal(x: int) -> bool:
    """
    Check if x is a pentagonal number.
    P_n = n(3n-1)/2 = x
    3n^2 - n - 2x = 0
    n = (1 + sqrt(1 + 24x)) / 6
    """
    if x <= 0:
        return False
    
    # Check if 1 + 24x is a perfect square
    disc = 1 + 24 * x
    root = math.isqrt(disc)
    
    if root * root != disc:
        return False
        
    # Check if (1 + root) is divisible by 6
    return (1 + root) % 6 == 0


@timeit
def solve():
    """
    Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference are pentagonal 
    and D = |P_k - P_j| is minimised; what is the value of D?
    """
    # Pentagonal numbers generator or list?
    # Since we don't know the upper bound, let's generate them on the fly.
    pentagonals = []
    
    # Start checking
    k = 1
    
    # We store the found minimum D to ensure it is indeed the minimum
    min_d = None
    
    while True:
        # Generate P_k
        p_k = k * (3 * k - 1) // 2
        pentagonals.append(p_k)
        
        # Check against all P_j where j < k
        # We iterate backwards from j = k-1 down to 0 to find smaller differences first?
        # Actually, iterating backwards (checking P_k - P_j) means we check smallest differences relative to P_k first?
        # No, P_k - P_(k-1) is the smallest difference for a fixed k.
        
        # Optimization:
        # If we have a candidate min_d, and the smallest possible difference for this k (which is P_k - P_{k-1})
        # is already larger than min_d, then no pair (P_k, P_j) can produce a difference smaller than min_d.
        # Since gaps grow with k, subsequent k's will also have larger gaps.
        # So we can safely terminate.
        
        if min_d is not None:
            # Smallest gap for current k is P_k - P_{k-1}
            # P_k - P_{k-1} = (3k^2 - k)/2 - (3(k-1)^2 - (k-1))/2 = 3k - 2
            smallest_gap = 3 * k - 2
            if smallest_gap > min_d:
                return min_d

        # Check existing pentagonals P_j
        # We iterate backwards: P_j = pentagonals[k-2], pentagonals[k-3]...
        # Indices in list: 0 to k-1. pentagonals[k-1] is P_k.
        # We want pentagonals[j] where j from k-2 down to 0.
        for j in range(k - 2, -1, -1):
            p_j = pentagonals[j]
            
            diff = p_k - p_j
            
            # Optimization: If we already found a min_d, and this diff is larger,
            # we don't need to check further for this P_j? 
            # No, because diff increases as j decreases.
            # If diff > min_d, we can stop checking THIS k, because smaller j will give larger diffs.
            if min_d is not None and diff >= min_d:
                break
                
            if is_pentagonal(diff):
                sum_val = p_k + p_j
                if is_pentagonal(sum_val):
                    # Found a valid pair!
                    # Since we iterate k upwards, and within k we check P_j downwards (diff increases),
                    # the first one we find for a fixed k is the smallest diff FOR THAT k.
                    # But is it the global minimum?
                    # We record it and let the outer loop termination condition decide.
                    if min_d is None or diff < min_d:
                        min_d = diff
                        # We might want to print it to see progress
                        # print(f"Found candidate: P_k={p_k}, P_j={p_j}, D={diff}")

        k += 1

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")