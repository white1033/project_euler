from euler.problems.p0010_summation_of_primes.solution import solve

def test_p0010_example():
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    assert solve(limit=10) == 17

def test_p0010_solution():
    assert solve() == 142913828922
