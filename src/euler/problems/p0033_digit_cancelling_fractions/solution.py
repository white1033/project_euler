'''
Problem 33: Digit Cancelling Fractions
'''
import time
import math
from fractions import Fraction
from euler.utils.common import timeit

@timeit
def solve() -> int:
    """
    Find the value of the denominator of the product of the four non-trivial examples.
    Brute-force approach.
    """
    product = Fraction(1, 1)
    
    for d in range(10, 100):
        for n in range(10, d):
            # Trivial examples like 30/50 are excluded.
            if n % 10 == 0 and d % 10 == 0:
                continue
                
            n_str = str(n)
            d_str = str(d)
            
            common = set(n_str) & set(d_str)
            
            if not common:
                continue
                
            for digit in common:
                n_list = list(n_str)
                d_list = list(d_str)
                
                n_list.remove(digit)
                d_list.remove(digit)
                
                if d_list[0] == '0':
                    continue
                    
                new_n = int(n_list[0])
                new_d = int(d_list[0])
                
                if new_d == 0:
                    continue
                
                if Fraction(n, d) == Fraction(new_n, new_d):
                    product *= Fraction(n, d)
                    break
                    
    return product.denominator

@timeit
def solve_algebraic() -> int:
    """
    Find the value of the denominator of the product of the four non-trivial examples.
    Algebraic approach.
    Consider n = 10a + c, d = 10c + b.
    (10a + c) / (10c + b) = a / b
    => b(10a + c) = a(10c + b)
    => 10ab + bc = 10ac + ab
    => 9ab = 10ac - bc = c(10a - b)
    => c = 9ab / (10a - b)
    """
    product = Fraction(1, 1)
    
    for a in range(1, 10):
        for b in range(1, 10):
            if a == b: continue # Trivial n=d or gives c=a (e.g. 22/22)
            
            # We want n < d, so (10a+c) < (10c+b).
            # From formula, if a < b, then 10a - b < 10a - a = 9a.
            # c = 9ab / (10a - b) > 9ab / 9a = b.
            # So c > b > a.
            # If c > b, then 10c + b > 10a + c is likely true.
            # Let's just calculate c and check constraints.
            
            numerator = 9 * a * b
            denominator = 10 * a - b
            
            if denominator == 0: continue
            
            if numerator % denominator == 0:
                c = numerator // denominator
                if 1 <= c <= 9:
                    # Valid digit c found
                    n = 10 * a + c
                    d = 10 * c + b
                    
                    # Check n < d constraint
                    if n < d:
                        product *= Fraction(n, d)
                        
    return product.denominator

if __name__ == "__main__":
    print("Running Brute Force:")
    result_bf = solve()
    print(f"Result: {result_bf}")
    
    print("\nRunning Algebraic:")
    result_alg = solve_algebraic()
    print(f"Result: {result_alg}")
