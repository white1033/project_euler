"""
Problem 40: Champernowne's Constant
"""

from euler.utils.common import timeit


def get_champernowne_digit(n: int) -> int:
    """
    Returns the n-th digit of Champernowne's constant.
    Uses range estimation to find the digit in O(log n) time.
    """
    if n < 1:
        raise ValueError("Index must be >= 1")

    # Range properties
    # 1-digit numbers: 1 to 9 (9 numbers)
    # 2-digit numbers: 10 to 99 (90 numbers)
    # k-digit numbers: 10^(k-1) to 10^k - 1 (9 * 10^(k-1) numbers)
    
    digits_per_number = 1
    count = 9
    
    # Step 1: Find which range n falls into
    while n > digits_per_number * count:
        n -= digits_per_number * count
        digits_per_number += 1
        count *= 10
        
    # Step 2: Determine exactly which number contains the digit
    # The range starts at 10^(digits_per_number - 1)
    start_num = 10**(digits_per_number - 1)
    
    # (n-1) is used because n is 1-based index remaining in this range
    offset = (n - 1) // digits_per_number
    target_num = start_num + offset
    
    # Step 3: Find which digit within that number
    digit_index = (n - 1) % digits_per_number
    
    return int(str(target_num)[digit_index])


@timeit
def solve():
    """
    Find the value of the following expression:
    d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
    """
    indices = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
    result = 1
    
    for idx in indices:
        digit = get_champernowne_digit(idx)
        # print(f"d_{idx} = {digit}")
        result *= digit
        
    return result


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")