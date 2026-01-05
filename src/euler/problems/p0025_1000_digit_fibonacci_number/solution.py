'''
Problem 25: 1000-digit Fibonacci Number
'''
import math

from euler.utils.common import timeit


@timeit
def solve(n_digits: int = 1000) -> int:
    """
    Finds the index of the first term in the Fibonacci sequence to contain n_digits.
    Uses Binet's formula and logarithms:
    F_n approx phi^n / sqrt(5)
    digits = floor(log10(F_n)) + 1
    We want digits >= n_digits, so log10(F_n) >= n_digits - 1
    
    n * log10(phi) - 0.5 * log10(5) >= n_digits - 1
    n >= (n_digits - 1 + 0.5 * log10(5)) / log10(phi)
    """
    if n_digits == 1:
        return 1
        
    phi = (1 + math.sqrt(5)) / 2
    log_phi = math.log10(phi)
    log_sqrt5 = 0.5 * math.log10(5)
    
    # inequality: n * log_phi - log_sqrt5 >= n_digits - 1
    # n * log_phi >= n_digits - 1 + log_sqrt5
    n = (n_digits - 1 + log_sqrt5) / log_phi
    
    return math.ceil(n)

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
