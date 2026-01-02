"""
Problem 38: Pandigital Multiples
"""

from euler.utils.common import timeit


def is_pandigital_1_to_9(s: str) -> bool:
    """Check if string contains digits 1-9 exactly once."""
    if len(s) != 9:
        return False
    return sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


@timeit
def solve():
    """
    Find the largest 1 to 9 pandigital 9-digit number formed as the concatenated product 
    of an integer with (1, 2, ... , n) where n > 1.
    """
    # Based on analysis:
    # 1. To beat the example 918273645, the number must start with 9.
    # 2. X cannot be 2 digits (90-99): n=3 -> 9 digits? 9x + 18x + 27x -> 2+3+3 = 8 digits. Too short.
    #                                   n=4 -> 11 digits. Too long.
    # 3. X cannot be 3 digits (900-999): n=2 -> 3+4=7 digits. Too short.
    #                                    n=3 -> 3+4+4=11 digits. Too long.
    # 4. X can be 4 digits (9000-9999): n=2 -> 4+5=9 digits. PERFECT.
    # 5. X cannot be >= 5 digits: n=2 -> 5+5=10 digits. Too long.
    #
    # So we only need to check 4-digit numbers starting with 9.
    # We search downwards from 9876 to 9123 to find the largest one first.
    
    for i in range(9876, 9123, -1):
        # Concatenated product of i and (1, 2)
        concatenated = str(i) + str(i * 2)
        
        if is_pandigital_1_to_9(concatenated):
            return int(concatenated)

    # Fallback to the example provided in the problem if no 4-digit solution is found
    return 918273645


if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")