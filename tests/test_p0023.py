from euler.problems.p0023_non_abundant_sums.solution import solve
from euler.utils.primes import sum_proper_divisors


def test_p0023_abundant_property():
    # 12 is smallest abundant number
    assert sum_proper_divisors(12) == 16
    assert 16 > 12
    
def test_p0023_solution():
    assert solve() == 4179871
