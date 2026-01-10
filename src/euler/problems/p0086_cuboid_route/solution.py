import math

from euler.utils.common import timeit


@timeit
def solve() -> int:
    limit = 1_000_000
    count = 0
    m = 0

    while count <= limit:
        m += 1
        for s in range(2, 2 * m + 1):
            if math.isqrt(m * m + s * s) ** 2 == m * m + s * s:
                if s <= m:
                    count += s // 2
                else:
                    count += m - (s + 1) // 2 + 1

    return m


if __name__ == "__main__":
    print(solve())
