from collections import Counter

from euler.utils.common import timeit


def is_same_digits(n1: int, n2: int) -> bool:
    """
    Checks if two numbers contain exactly the same digits.
    Using Counter (or sorted string) is efficient enough for small number of digits.
    Since we are dealing with integers, we can convert to string.
    """
    return Counter(str(n1)) == Counter(str(n2))

@timeit
def solve() -> int:
    """
    Finds the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    """
    # Start checking from 1-digit numbers, then 2-digit, etc.
    # We know x and 6x must have the same number of digits.
    # Therefore, x must start with '1' (since 2*10^k * 6 > 10^(k+1)).
    # Range for d-digit number: [10^(d-1), 10^d // 6]
    
    # Mathematical optimization:
    # If x and k*x are permutations, they have the same digit sum.
    # Two numbers with the same digit sum are congruent modulo 9.
    # So x == 2x (mod 9) => x == 0 (mod 9).
    # Thus, x must be a multiple of 9.
    
    d = 1
    while True:
        start = 10**(d - 1)
        end = (10**d) // 6 + 1
        
        # Adjust start to be the first multiple of 9 >= start
        if start % 9 != 0:
            start += (9 - (start % 9))
            
        for x in range(start, end, 9):
            # Check 6x first as it's the most restrictive (changes value the most)
            # Then check others.
            digits_x = Counter(str(x))
            
            if (Counter(str(6 * x)) == digits_x and
                Counter(str(5 * x)) == digits_x and
                Counter(str(4 * x)) == digits_x and
                Counter(str(3 * x)) == digits_x and
                Counter(str(2 * x)) == digits_x):
                return x
        
        d += 1

if __name__ == "__main__":
    print(solve())