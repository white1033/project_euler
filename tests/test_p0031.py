from euler.problems.p0031_coin_sums.solution import solve

def test_p0031_example():
    # Example logic: How many ways to make 5p?
    # 1. 1x5p
    # 2. 2x2p + 1x1p
    # 3. 1x2p + 3x1p
    # 4. 5x1p
    # Total = 4 ways
    assert solve(target=5) == 4

def test_p0031_solution():
    assert solve() == 73682
