from euler.problems.p0060_prime_pair_sets.solution import (
    find_clique,
    is_pair_prime,
    sieve_of_eratosthenes,
    solve,
)


def test_prime_pair_check():
    """
    Test the concatenation check with the example provided in the problem.
    Set: {3, 7, 109, 673}
    """
    example_set = [3, 7, 109, 673]
    
    # Check pairwise validity
    for i in range(len(example_set)):
        for j in range(i + 1, len(example_set)):
            p1, p2 = example_set[i], example_set[j]
            assert is_pair_prime(p1, p2), f"Failed for pair ({p1}, {p2})"

    # Check a known invalid pair (e.g., 2 and 3 -> 23 is prime, but 32 is not)
    # Actually 2 is excluded, let's try 3 and 5 -> 35 (div by 5)
    assert not is_pair_prime(3, 5)

def test_find_clique_size_4():
    """
    Verify that the algorithm can find the example set of size 4.
    """
    # Generate primes up to 1000 (enough to cover 3, 7, 109, 673)
    primes = sieve_of_eratosthenes(1000)
    primes = [p for p in primes if p != 2 and p != 5]
    
    # The example set {3, 7, 109, 673} should be findable
    # We force the start with [3] to guide the search
    
    # Primes must include the target set
    candidates = [p for p in primes if p > 3]
    
    # Try to find a clique of size 4 starting with [3]
    result = find_clique([3], candidates, 4)
    
    # Note: It might find {3, 7, 109, 673} OR another valid set of size 4 involving 3.
    # But {3, 7, 109, 673} is the one with the lowest sum (792).
    # Let's just check if it returns a valid clique of size 4 including 3.
    
    assert result is not None
    assert len(result) == 4
    assert result[0] == 3
    
    # Verify the clique property for the result
    for i in range(4):
        for j in range(i + 1, 4):
            assert is_pair_prime(result[i], result[j])

def test_solution():
    """Test the final solution for Problem 60."""
    # This might take a few seconds, so it's a real integration test
    assert solve() == 26033
