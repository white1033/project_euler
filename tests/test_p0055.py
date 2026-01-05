from euler.problems.p0055_lychrel_numbers.solution import is_lychrel, solve


def test_examples():
    # 47 becomes 121 in 1 iteration
    assert is_lychrel(47) is False
    
    # 349 becomes 7337 in 3 iterations
    assert is_lychrel(349) is False
    
    # 196 is the first Lychrel number (by problem definition assumption)
    assert is_lychrel(196) is True

def test_solution():
    """
    Test the final solution for Problem 55.
    """
    assert solve() == 249
