from euler.problems.p0009_special_pythagorean_triplet.solution import solve


def test_p0009_example():
    # 3^2 + 4^2 = 5^2, sum = 12, product = 60
    assert solve(target_sum=12) == 60

def test_p0009_solution():
    assert solve() == 31875000
