from euler.problems.p0012_highly_divisible_triangular_number.solution import solve


def test_p0012_example():
    # 28 is the first triangle number to have over five divisors.
    # Note: solve(target) finds the first one having > target divisors.
    assert solve(target_divisors=5) == 28

def test_p0012_solution():
    assert solve() == 76576500
