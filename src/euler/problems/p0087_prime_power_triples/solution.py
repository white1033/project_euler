from euler.utils.common import timeit
from euler.utils.primes import sieve_of_eratosthenes


@timeit
def solve() -> int:
    limit = 50_000_000

    primes = sieve_of_eratosthenes(7100)

    squares = []
    cubes = []
    fourths = []

    for p in primes:
        p2 = p * p
        if p2 >= limit:
            break
        squares.append(p2)

    for p in primes:
        p3 = p * p * p
        if p3 >= limit:
            break
        cubes.append(p3)

    for p in primes:
        p4 = p * p * p * p
        if p4 >= limit:
            break
        fourths.append(p4)

    sums = set()

    for c in fourths:
        for b in cubes:
            if b + c >= limit:
                break
            for a in squares:
                val = a + b + c
                if val < limit:
                    sums.add(val)
                else:
                    break

    return len(sums)


if __name__ == "__main__":
    print(solve())
