from euler.utils.common import timeit


@timeit
def solve() -> int:
    x = 1
    y = 1
    limit = 10**12

    while True:
        n = (x + 1) // 2

        if n > limit:
            b = (y + 1) // 2
            return b

        next_x = 3 * x + 4 * y
        next_y = 2 * x + 3 * y
        x, y = next_x, next_y


if __name__ == "__main__":
    print(solve())
