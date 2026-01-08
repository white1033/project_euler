from euler.problems.p0076_counting_summations.solution import solve


def test_p0076_example():
    # Example from problem description:
    # 5 can be written as a sum in exactly 6 different ways.
    # Note: The problem asks for "at least two positive integers",
    # so we exclude the number itself (e.g. 5 = 5).
    assert solve(5) == 6


def test_p0076_solution():
    result = solve(100)
    print(f"\nSolution for Problem 76: {result}")
    # We don't know the answer yet, but it should be a positive integer
    assert result > 0
