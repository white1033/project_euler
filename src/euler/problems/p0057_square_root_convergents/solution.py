from euler.utils.common import timeit
import math

def get_next_convergent(n: int, d: int) -> tuple[int, int]:
    """
    Given the current convergent n/d for sqrt(2),
    returns the next convergent using the relation:
    next_n / next_d = (n + 2d) / (n + d)
    """
    return n + 2 * d, n + d

@timeit
def solve() -> int:
    """
    Calculates how many of the first 1000 expansions of sqrt(2)
    have a numerator with more digits than the denominator.
    """
    count = 0
    n, d = 3, 2  # The first expansion: 1 + 1/2 = 3/2

    for _ in range(1, 1001): # Loop 1000 times checking the current convergent
        if len(str(n)) > len(str(d)):
            count += 1
        
        n, d = get_next_convergent(n, d)
        
    return count

if __name__ == "__main__":
    print(solve())