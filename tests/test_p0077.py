from euler.problems.p0077_prime_summations.solution import solve


def test_p0077_example():
    # 10 is the first value with > 4 ways (it has exactly 5 ways)
    assert solve(4) == 10


def test_p0077_solution():
    result = solve()
    print(f"\nSolution for Problem 77: {result}")
    assert result > 0
