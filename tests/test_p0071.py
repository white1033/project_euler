from euler.problems.p0071_ordered_fractions.solution import solve


def test_p0071_basic_case():
    """
    Test with the example given in the problem description:
    For d <= 8, the fraction immediately to the left of 3/7 is 2/5.
    The numerator is 2.
    """
    assert solve(8) == 2


def test_p0071_solution():
    """
    Test the full solution.
    """
    assert solve(1000000) == 428570
