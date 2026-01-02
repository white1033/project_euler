from euler.problems.p0035_circular_primes.solution import solve

def test_p0035_example():
    # There are thirteen such primes below 100
    assert solve(limit=100) == 13

def test_p0035_solution():
    assert solve() == 55
