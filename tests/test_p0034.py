import math

from euler.problems.p0034_digit_factorials.solution import solve


def test_p0034_curious_number():
    # 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
    digits = [1, 4, 5]
    assert sum(math.factorial(d) for d in digits) == 145

def test_p0034_solution():
    assert solve() == 40730
