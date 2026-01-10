from euler.utils.common import timeit


@timeit
def solve() -> int:
    limit = 1_000_000_000
    total_perimeter = 0

    # Pell equation x^2 - 3y^2 = 1
    # Fundamental solution (2, 1)
    x, y = 2, 1

    sign = 1

    while True:
        next_x = 2 * x + 3 * y
        next_y = x + 2 * y
        x, y = next_x, next_y

        if sign == 1:
            if (2 * x + 1) % 3 == 0:
                a = (2 * x + 1) // 3
                perimeter = 3 * a + 1
            else:
                sign *= -1
                continue
        else:
            if (2 * x - 1) % 3 == 0:
                a = (2 * x - 1) // 3
                perimeter = 3 * a - 1
            else:
                sign *= -1
                continue

        if perimeter > limit:
            break

        if a > 1:
            total_perimeter += perimeter

        sign *= -1

    return total_perimeter


if __name__ == "__main__":
    print(solve())
