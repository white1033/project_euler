'''
Problem 17: Number Letter Counts
'''
from euler.utils.common import timeit

# Word lengths
# 0 (unused), 1..9
ONES_LENGTHS = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4] 
# 10..19
TEENS_LENGTHS = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# 20, 30, ..., 90
TENS_LENGTHS = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

def count_letters(n: int) -> int:
    if n == 1000:
        return 3 + 8 # one thousand
    
    length = 0
    
    # Hundreds
    if n >= 100:
        length += ONES_LENGTHS[n // 100] + 7 # X hundred
        n %= 100
        if n > 0:
            length += 3 # and
            
    # Tens and Ones (0-99)
    if n > 0:
        if n < 10:
            length += ONES_LENGTHS[n]
        elif n < 20:
            length += TEENS_LENGTHS[n - 10]
        else:
            length += TENS_LENGTHS[n // 10]
            length += ONES_LENGTHS[n % 10]
            
    return length

@timeit
def solve(limit: int = 1000) -> int:
    """
    If all the numbers from 1 to limit inclusive were written out in words, how many letters would be used?
    """
    return sum(count_letters(i) for i in range(1, limit + 1))

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
