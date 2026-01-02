'''
Problem 24: Lexicographic Permutations
'''
import math
from euler.utils.common import timeit

@timeit
def solve(nth: int = 1_000_000, digits: list[int] = None) -> str:
    """
    Finds the nth lexicographic permutation of the given digits.
    Uses the Factorial Number System (Factoradic) approach.
    """
    if digits is None:
        digits = list(range(10))
        
    # We want the nth permutation. Since permutations are 0-indexed in logic usually,
    # but the problem asks for "1st", "2nd"... "millionth".
    # If we want the 1st, we want index 0. So we subtract 1.
    target_index = nth - 1
    
    available_digits = sorted(digits) # Ensure sorted for lexicographic order
    result = ""
    
    n_digits = len(available_digits)
    
    for i in range(n_digits):
        # We are looking for the digit at position i
        # The number of permutations for the remaining digits is (n_digits - 1 - i)!
        
        block_size = math.factorial(n_digits - 1 - i)
        
        # Which block are we in?
        selected_index = target_index // block_size
        
        # Add the digit to result and remove from available
        digit = available_digits.pop(selected_index)
        result += str(digit)
        
        # Update target_index for the next iteration
        target_index %= block_size
        
    return result

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
