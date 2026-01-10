from euler.utils.common import timeit
from itertools import combinations


@timeit
def solve() -> int:
    digits = list(range(10))
    cubes = list(combinations(digits, 6))
    n = len(cubes)

    count = 0

    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

    def has_digit(cube, d):
        if d in cube:
            return True
        if d == 6 and 9 in cube:
            return True
        if d == 9 and 6 in cube:
            return True
        return False

    def check(c1, c2):
        for d1, d2 in squares:
            can_form = (has_digit(c1, d1) and has_digit(c2, d2)) or (
                has_digit(c2, d1) and has_digit(c1, d2)
            )
            if not can_form:
                return False
        return True

    for i in range(n):
        for j in range(i, n):
            c1 = cubes[i]
            c2 = cubes[j]
            if check(c1, c2):
                count += 1

    return count


if __name__ == "__main__":
    print(solve())
