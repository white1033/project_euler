from euler.problems.p0025_1000_digit_fibonacci_number.solution import solve

def test_p0025_example():
    # The 12th term is the first to contain 3 digits
    assert solve(n_digits=3) == 12

def test_p0025_solution():
    assert solve() == 4782
