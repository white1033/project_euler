from euler.utils.common import timeit


@timeit
def solve() -> int:
    size = 50
    count = 0

    points = []
    for x in range(size + 1):
        for y in range(size + 1):
            if x == 0 and y == 0:
                continue
            points.append((x, y))

    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            d_op2 = x1 * x1 + y1 * y1
            d_oq2 = x2 * x2 + y2 * y2
            d_pq2 = (x1 - x2) ** 2 + (y1 - y2) ** 2

            if d_op2 + d_oq2 == d_pq2 or d_op2 + d_pq2 == d_oq2 or d_oq2 + d_pq2 == d_op2:
                count += 1

    return count


if __name__ == "__main__":
    print(solve())
