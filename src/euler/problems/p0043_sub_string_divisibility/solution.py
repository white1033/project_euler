"""
Problem 43: Sub-string Divisibility
"""

from euler.utils.common import timeit


def get_candidates(divisor: int) -> list[str]:
    """Generate 3-digit strings (including leading zeros) divisible by divisor."""
    candidates = []
    for i in range(0, 1000, divisor):
        candidates.append(f"{i:03d}")
    return candidates


@timeit
def solve():
    """
    Find the sum of all 0 to 9 pandigital numbers with the sub-string divisibility property.
    """
    # Divisors for the sub-strings starting from d2d3d4 to d8d9d10
    # d2..d4 % 2 == 0
    # d3..d5 % 3 == 0
    # d4..d6 % 5 == 0
    # d5..d7 % 7 == 0
    # d6..d8 % 11 == 0
    # d7..d9 % 13 == 0
    # d8..d10 % 17 == 0
    
    divisors = [2, 3, 5, 7, 11, 13, 17]
    
    # We build from the back (d8d9d10 divisible by 17)
    # Current candidates are the suffixes matching the last condition
    current_suffixes = get_candidates(17)
    
    # Iterate backwards through the divisors (13, 11, 7, 5, 3, 2)
    # We skip 17 because we used it to initialize
    for div in reversed(divisors[:-1]):
        new_suffixes = []
        for suffix in current_suffixes:
            # Suffix is like 'd_k ... d_10'
            # We need to prepend a digit 'd_(k-1)'
            # Such that 'd_(k-1) d_k d_(k+1)' is divisible by div
            
            # The 'tail' for the check is the first two digits of the current suffix
            check_tail = suffix[:2] 
            
            for digit in "0123456789":
                # Optimization: Pandigital constraint check early?
                # Actually, checking uniqueness at every step is good pruning.
                if digit in suffix:
                    continue
                
                # Form the 3-digit number to check
                num_to_check = int(digit + check_tail)
                
                if num_to_check % div == 0:
                    new_suffixes.append(digit + suffix)
        
        current_suffixes = new_suffixes
    
    # Now we have strings from d2...d10. 
    # We need to add d1. 
    # The number must be 0-9 pandigital.
    total_sum = 0
    for suffix in current_suffixes:
        # Find the missing digit for d1
        all_digits = set("0123456789")
        used_digits = set(suffix)
        missing = all_digits - used_digits
        
        if len(missing) == 1:
            d1 = missing.pop()
            # d1 cannot be '0' if we consider strictly 10-digit numbers without leading zeros.
            # However, problem says "0 to 9 pandigital number", usually implies 10 digits.
            # Example 1406357289 is given in problem (starts with 1).
            # If d1 is 0, it's a 9 digit number technically. 
            # But the problem treats them as strings of digits d1..d10.
            # Let's check if 0 can be leading. 
            # The first example in the problem description usually clarifies.
            # Re-reading: "The number, 1406357289, is a 0 to 9 pandigital number..."
            # It doesn't explicitly forbid leading zero, but usually pandigital numbers d1..d10 implies d1!=0.
            # However, logic: if d1=0, d2d3d4 must be div by 2.
            # Let's assume d1 != 0 first, but simply summing them up handles the value correctly.
            # Wait, if d1 is 0, the value is just the integer value.
            # Let's assume valid d1 cannot be 0 for a "10-digit number".
            # But wait, looking at typical Project Euler constraints, if it asks for a "0 to 9 pandigital number", 
            # and describes d1..d10, d1=0 would make it a 9-digit number.
            # Let's allow 0 for now? No, usually 'n-digit number' implies no leading zero.
            # Let's look at the example: 1406357289.
            # Let's assume standard rule: No leading zeros for the full number.
            if d1 != '0':
                full_num_str = d1 + suffix
                total_sum += int(full_num_str)
                
    return total_sum


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")