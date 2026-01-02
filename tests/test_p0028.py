from euler.problems.p0028_number_spiral_diagonals.solution import solve

def test_p0028_example():
    # 5x5 spiral sum is 101
    assert solve(size=5) == 101

def test_p0028_solution():
    assert solve() == 669171001
