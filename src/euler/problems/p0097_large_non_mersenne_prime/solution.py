from euler.utils.common import timeit


@timeit
def solve() -> int:
    mod = 10_000_000_000

    exponent = 7830457
    multiplier = 28433

    power_part = pow(2, exponent, mod)

    result = (multiplier * power_part + 1) % mod

    return result


if __name__ == "__main__":
    print(solve())
