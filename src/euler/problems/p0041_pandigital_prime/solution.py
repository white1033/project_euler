"""
Problem 41: Pandigital Prime
"""

from itertools import permutations

from euler.utils.common import timeit
from euler.utils.primes import is_prime


@timeit
def solve():
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    What is the largest n-digit pandigital prime that exists?
    """
    # Analysis based on divisibility by 3 (sum of digits rule):
    # n=9: sum=45 (divisible by 3) -> Not prime
    # n=8: sum=36 (divisible by 3) -> Not prime
    # n=7: sum=28 (not divisible by 3) -> Possible primes!
    # n=6: sum=21 (divisible by 3) -> Not prime
    # n=5: sum=15 (divisible by 3) -> Not prime
    # n=4: sum=10 (not divisible by 3) -> Possible primes!
    
    # Since we want the *largest*, we start checking from n=7.
    # We generate permutations of "7654321" in descending order.
    # The first prime we encounter is the largest.
    
    # Check n=7
    digits_7 = '7654321'
    for p in permutations(digits_7):
        num_str = "".join(p)
        num = int(num_str)
        if is_prime(num):
            return num
            
    # Fallback to n=4 if no 7-digit pandigital prime exists (though one definitely does)
    digits_4 = '4321'
    for p in permutations(digits_4):
        num_str = "".join(p)
        num = int(num_str)
        if is_prime(num):
            return num
            
    return None


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")