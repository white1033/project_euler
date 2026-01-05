from euler.problems.p0062_cubic_permutations.solution import solve


def test_p0062_example():
    # The example says 41063625 (345^3) is the smallest cube with exactly 3 permutations
    assert solve(target_permutations=3) == 41063625

def test_p0062_solution():
    # We verify the solution for 5 permutations works and produces a value.
    # The known answer is 127035954683.
    assert solve(target_permutations=5) == 127035954683
