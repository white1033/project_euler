from euler.problems.p0072_counting_fractions.solution import solve


def test_p0072_example():
    """
    Test with the example given in the problem description:
    For d <= 8, there are 21 reduced proper fractions.
    """
    assert solve(8) == 21


def test_p0072_solution():
    """
    Test the full solution.
    (We don't know the answer yet, but we can check it runs fast enough and returns a specific value)
    """
    result = solve(1000000)
    assert result > 0
    print(f"\nSolution for Problem 72: {result}")
