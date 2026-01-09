from euler.problems.p0058_spiral_primes.solution import solve
from euler.utils.primes import is_prime


def test_example_case():
    """
    Verify the example given in the problem:
    For side length 7, the ratio is 8/13 ~ 62%.
    """
    prime_count = 0
    total_count = 1
    s = 1

    # Simulate up to s = 7
    while s < 7:
        s += 2
        step = s - 1
        bottom_right = s * s

        c1 = bottom_right - step
        c2 = bottom_right - 2 * step
        c3 = bottom_right - 3 * step

        if is_prime(c1):
            prime_count += 1
        if is_prime(c2):
            prime_count += 1
        if is_prime(c3):
            prime_count += 1

        total_count += 4

    assert s == 7
    assert total_count == 13
    assert prime_count == 8
    assert abs(prime_count / total_count - 8 / 13) < 1e-9


def test_solution():
    """Test the final solution for Problem 58."""
    assert solve() == 26241
