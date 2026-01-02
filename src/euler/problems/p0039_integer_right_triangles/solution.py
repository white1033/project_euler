"""
Problem 39: Integer Right Triangles
"""

from euler.utils.common import timeit


@timeit
def solve():
    """
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.
    For which value of p <= 1000, is the number of solutions maximised?
    """
    max_solutions = 0
    best_p = 0
    
    # Optimization 1: Perimeter of an integer right triangle is always even.
    # Proof: a^2 + b^2 = c^2.
    # - If a, b are both even, c is even -> p = even + even + even = even.
    # - If one is odd, one even, c is odd -> p = odd + even + odd = even.
    # - If both odd, c^2 is even (divisible by 2 but not 4), impossible for square.
    for p in range(12, 1001, 2):
        solutions = 0
        
        # From a^2 + b^2 = c^2 and c = p - a - b, we can derive:
        # b = (p^2 - 2pa) / (2p - 2a)
        # Since a < c and b < c, a < p/2. Also assuming a <= b, a < p/3 is a safe upper bound estimate,
        # but iterating to p/2 is safe enough with the break condition.
        # Actually a < p/3 is strict because if a >= p/3, then b >= a >= p/3, so c > p/3 => a+b+c > p.
        for a in range(1, p // 3):
            # Check if b is an integer
            numerator = p * (p - 2 * a)
            denominator = 2 * (p - a)
            
            if numerator % denominator == 0:
                solutions += 1
                
        if solutions > max_solutions:
            max_solutions = solutions
            best_p = p
            
    return best_p


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")