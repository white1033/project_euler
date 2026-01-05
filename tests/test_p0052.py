from euler.problems.p0052_permuted_multiples.solution import is_same_digits, solve


def test_is_same_digits():
    """
    Test the helper function for checking permutations.
    """
    # Example from problem description
    assert is_same_digits(125874, 251748) is True
    
    # Simple cases
    assert is_same_digits(123, 321) is True
    assert is_same_digits(123, 124) is False
    assert is_same_digits(123, 1234) is False # Different length

def test_solution():
    """
    Test the final solution for Problem 52.
    """
    assert solve() == 142857
