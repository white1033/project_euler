from euler.utils.primes import sieve_totient


def solve(limit: int = 1000000) -> int:
    """
    How many elements would be contained in the set of reduced proper fractions for d <= limit?

    This is equivalent to summing Euler's totient function phi(d) for 2 <= d <= limit.
    """
    phi = sieve_totient(limit)

    # We sum phi(d) for d from 2 to limit.
    # phi[0] is 0, phi[1] is 1, but reduced proper fractions require n < d.
    # For d=1, n < 1 and n positive integer is impossible. So we start from d=2.
    return sum(phi[2:])
