from euler.problems.p0007_10001st_prime.solution import solve


def test_p0007_example():
    assert solve(n=6) == 13

def test_p0007_first_prime():
    assert solve(n=1) == 2

def test_p0007_solution():
    assert solve() == 104743
