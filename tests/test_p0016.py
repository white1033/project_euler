from euler.problems.p0016_power_digit_sum.solution import solve

def test_p0016_example():
    # 2^15 = 32768, sum = 3+2+7+6+8 = 26
    assert solve(exponent=15) == 26

def test_p0016_solution():
    assert solve() == 1366
