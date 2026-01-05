from euler.problems.p0020_factorial_digit_sum.solution import solve


def test_p0020_example():
    # 10! = 3628800, sum = 27
    assert solve(n=10) == 27

def test_p0020_solution():
    assert solve() == 648
