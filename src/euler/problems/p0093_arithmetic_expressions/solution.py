from euler.utils.common import timeit
from itertools import combinations, permutations, product
import operator


@timeit
def solve() -> int:
    digits = list(range(10))
    digit_sets = list(combinations(digits, 4))

    ops = [operator.add, operator.sub, operator.mul, operator.truediv]

    max_consecutive = 0
    best_set = 0

    for s in digit_sets:
        results = set()
        for p in permutations(s):
            for op1, op2, op3 in product(ops, repeat=3):
                a, b, c, d = p[0], p[1], p[2], p[3]

                try:
                    res = op3(op2(op1(a, b), c), d)
                    if res > 0 and abs(res - round(res)) < 1e-9:
                        results.add(round(res))
                except ZeroDivisionError:
                    pass

                try:
                    res = op3(op1(a, op2(b, c)), d)
                    if res > 0 and abs(res - round(res)) < 1e-9:
                        results.add(round(res))
                except ZeroDivisionError:
                    pass

                try:
                    res = op1(a, op3(op2(b, c), d))
                    if res > 0 and abs(res - round(res)) < 1e-9:
                        results.add(round(res))
                except ZeroDivisionError:
                    pass

                try:
                    res = op1(a, op2(b, op3(c, d)))
                    if res > 0 and abs(res - round(res)) < 1e-9:
                        results.add(round(res))
                except ZeroDivisionError:
                    pass

                try:
                    res = op2(op1(a, b), op3(c, d))
                    if res > 0 and abs(res - round(res)) < 1e-9:
                        results.add(round(res))
                except ZeroDivisionError:
                    pass

        n = 1
        while n in results:
            n += 1
        length = n - 1

        if length > max_consecutive:
            max_consecutive = length
            best_set = int("".join(map(str, s)))

    return best_set


if __name__ == "__main__":
    print(solve())
