import pytest
from euler.problems.p0051_prime_digit_replacements.solution import solve, get_family_size

def test_example_case_1():
    """
    Test the first example from the problem description:
    By replacing the 1st digit of the 2-digit number *3, 
    it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
    """
    pattern = "*3"
    family = get_family_size(pattern)
    assert len(family) == 6
    assert 13 in family
    assert 23 in family
    assert 33 not in family # 33 is not prime

def test_example_case_2():
    """
    Test the second example from the problem description:
    By replacing the 3rd and 4th digits of 56**3 with the same digit, 
    this 5-digit number is the first example having seven primes among the ten generated numbers.
    The family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
    """
    pattern = "56**3"
    family = get_family_size(pattern)
    assert len(family) == 7
    assert 56003 in family # The smallest member

def test_solution():
    """
    Test the final solution for Problem 51.
    """
    assert solve() == 121313
