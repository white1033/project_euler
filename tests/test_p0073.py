from euler.problems.p0073_counting_fractions_in_a_range.solution import solve


def test_p0073_example():
    """
    Test with the example given in the problem description:
    For d <= 8, there are 3 fractions between 1/3 and 1/2: 3/8, 2/5, 3/7.
    """
    assert solve(8) == 3


def test_p0073_solution():
    """
    Test the full solution.
    """
    result = solve(12000)
    assert result > 0
    print(f"\nSolution for Problem 73: {result}")
