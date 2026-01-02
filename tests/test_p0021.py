from euler.problems.p0021_amicable_numbers.solution import solve
from euler.utils.primes import sum_proper_divisors

def test_p0021_example():
    # d(220) = 284
    assert sum_proper_divisors(220) == 284
    # d(284) = 220
    assert sum_proper_divisors(284) == 220
    # 220 and 284 are amicable pair

def test_p0021_solution():
    assert solve() == 31626
