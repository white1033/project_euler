from euler.problems.p0029_distinct_powers.solution import solve


def test_p0029_example():
    # 2 <= a <= 5, 2 <= b <= 5 -> 15 distinct terms
    assert solve(limit=5) == 15

def test_p0029_solution():
    assert solve() == 9183
