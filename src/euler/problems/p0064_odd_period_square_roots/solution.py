import math


def solve(limit: int = 10000) -> int:
    """
    How many odd period square roots are there for N <= limit?
    """
    odd_period_count = 0
    
    for n in range(1, limit + 1):
        # 1. Check if perfect square
        root = math.isqrt(n)
        if root * root == n:
            continue
            
        # 2. Continued Fraction Algorithm
        # Initialize
        m = 0
        d = 1
        a0 = root
        a = a0
        
        period = 0
        
        # 3. Iterate until the cycle repeats
        # A property of sqrt(N) continued fractions is that the period ends 
        # when a_k = 2 * a0.
        while a != 2 * a0:
            m = d * a - m
            d = (n - m * m) // d
            a = (a0 + m) // d
            period += 1
            
        # 4. Check parity
        if period % 2 != 0:
            odd_period_count += 1
            
    return odd_period_count