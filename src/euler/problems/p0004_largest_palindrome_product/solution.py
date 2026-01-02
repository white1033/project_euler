'''
Problem 4: Largest Palindrome Product
'''
from euler.utils.common import timeit

def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

@timeit
def solve():
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    Uses optimization: 6-digit palindromes are divisible by 11.
    """
    max_palindrome = 0
    
    # Iterate downwards from 999
    for a in range(999, 99, -1):
        # Optimization: if a * a <= max_palindrome, we won't find a larger one
        # because b <= a.
        if a * a <= max_palindrome:
            break
            
        # Optimization: One of a or b must be divisible by 11 for 6-digit palindromes.
        # If a is not divisible by 11, b must be.
        start_b = a
        step_b = 1
        
        if a % 11 != 0:
            # Find the largest b <= a that is divisible by 11
            start_b = a - (a % 11)
            step_b = 11
            
        for b in range(start_b, 99, -step_b):
            product = a * b
            
            # Pruning
            if product <= max_palindrome:
                break
                
            if is_palindrome(product):
                max_palindrome = product
                
    return max_palindrome

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")