from euler.utils.common import timeit


@timeit
def solve() -> int:
    limit = 10_000_000

    max_next = 568
    destinations = [0] * max_next

    for i in range(1, max_next):
        curr = i
        while curr != 1 and curr != 89:
            s = 0
            temp = curr
            while temp > 0:
                d = temp % 10
                s += d * d
                temp //= 10
            curr = s
        destinations[i] = curr

    count = 0
    sq = [d * d for d in range(10)]

    for i in range(1, limit):
        s = 0
        temp = i
        while temp > 0:
            d = temp % 10
            s += sq[d]
            temp //= 10

        if destinations[s] == 89:
            count += 1

    return count


if __name__ == "__main__":
    print(solve())
