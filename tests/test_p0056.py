import pytest
from euler.problems.p0056_powerful_digit_sum.solution import solve, sum_digits

def test_sum_digits():
    """Test the digit sum helper function."""
    assert sum_digits(10**100) == 1 # A googol
    assert sum_digits(12345) == 15
    assert sum_digits(2**15) == 26 # 32768 -> 3+2+7+6+8 = 26

def test_solution():
    """Test the final solution for Problem 56."""
    assert solve() == 972
