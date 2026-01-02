"""
Problem 36: Double-base Palindromes
"""

from euler.utils.common import timeit


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def make_palindrome(k: int, odd_length: bool) -> int:
    s = str(k)
    if odd_length:
        return int(s + s[-2::-1])
    else:
        return int(s + s[::-1])


@timeit
def solve_brute_force():
    """
    Original approach: Iterate all odd numbers.
    Complexity: O(N)
    """
    limit = 1_000_000
    total_sum = 0
    for n in range(1, limit, 2):
        if is_palindrome(str(n)):
            if is_palindrome(f"{n:b}"):
                total_sum += n
    return total_sum


@timeit
def solve_generative():
    """
    Optimized approach: Generate Base 10 palindromes, then check Base 2.
    Complexity: O(sqrt(N)) - Generates ~2000 palindromes instead of checking 1,000,000 numbers.
    """
    limit = 1_000_000
    total_sum = 0

    # We generate palindromes from roots 1 to 999.
    # Case 1: Odd length palindromes (e.g., root 12 -> 121, root 999 -> 99999)
    # Case 2: Even length palindromes (e.g., root 12 -> 1221, root 999 -> 999999)
    
    for k in range(1, 1000):
        # Generate odd length palindrome
        p_odd = make_palindrome(k, odd_length=True)
        if p_odd < limit:
            # Check optimization: Base 2 palindrome must be odd.
            # Base 10 palindrome ending is same as starting digit.
            # So if p_odd is odd, it's worth checking.
            if p_odd % 2 != 0 and is_palindrome(f"{p_odd:b}"):
                total_sum += p_odd
        
        # Generate even length palindrome
        p_even = make_palindrome(k, odd_length=False)
        if p_even < limit:
            if p_even % 2 != 0 and is_palindrome(f"{p_even:b}"):
                total_sum += p_even

    return total_sum


def solve():
    # We return the optimized one as the main answer, 
    # but I kept brute_force above for manual comparison if desired.
    return solve_generative()


if __name__ == "__main__":
    print("Running Brute Force:")
    result_bf = solve_brute_force()
    print(f"Brute Force Result: {result_bf}\n")

    print("Running Generative (Optimized):")
    result_opt = solve_generative()
    print(f"Optimized Result: {result_opt}")
