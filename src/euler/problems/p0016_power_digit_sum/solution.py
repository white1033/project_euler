'''
Problem 16: Power Digit Sum
'''
from euler.utils.common import timeit


@timeit
def solve(exponent: int = 1000) -> int:
    """
    What is the sum of the digits of the number 2^exponent?
    """
    number = 2 ** exponent
    # Convert number to string, iterate over characters, convert back to int, and sum
    return sum(int(d) for d in str(number))

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
