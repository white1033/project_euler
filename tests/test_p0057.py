import pytest
from euler.problems.p0057_square_root_convergents.solution import solve, get_next_convergent

def test_get_next_convergent():
    """Test the recurrence relation for the first few expansions."""
    n, d = 3, 2
    
    # 2nd expansion
    n, d = get_next_convergent(n, d)
    assert (n, d) == (7, 5)
    
    # 3rd expansion
    n, d = get_next_convergent(n, d)
    assert (n, d) == (17, 12)
    
    # 4th expansion
    n, d = get_next_convergent(n, d)
    assert (n, d) == (41, 29)

def test_digit_count_condition():
    """
    Verify the problem statement's claim:
    'the eighth expansion, 1393/985, is the first example where 
    the number of digits in the numerator exceeds... denominator'
    """
    n, d = 3, 2
    # Check 1st to 7th
    for _ in range(1, 8):
        assert len(str(n)) <= len(str(d))
        n, d = get_next_convergent(n, d)
    
    # Check 8th (now n, d holds the 8th expansion values)
    assert (n, d) == (1393, 985)
    assert len(str(n)) > len(str(d))

def test_solution():
    """Test the final solution for Problem 57."""
    assert solve() == 153
