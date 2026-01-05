'''
Problem 20: Factorial Digit Sum
'''
import math

from euler.utils.common import timeit


@timeit
def solve(n: int = 100) -> int:
    """
    Find the sum of the digits in the number n!
    """
    number = math.factorial(n)
    return sum(int(d) for d in str(number))

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
