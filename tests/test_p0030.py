from euler.problems.p0030_digit_fifth_powers.solution import solve


def test_p0030_example():
    # Sum of numbers written as sum of 4th powers of their digits
    # 1634, 8208, 9474 -> sum = 19316
    assert solve(power=4) == 19316

def test_p0030_solution():
    assert solve() == 443839
