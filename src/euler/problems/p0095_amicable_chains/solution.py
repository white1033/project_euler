from euler.utils.common import timeit


@timeit
def solve() -> int:
    limit = 1_000_000

    div_sum = [1] * (limit + 1)
    div_sum[0] = 0

    for i in range(2, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            div_sum[j] += i

    max_len = 0
    min_elem = 0

    visited_global = [False] * (limit + 1)

    for i in range(2, limit + 1):
        if visited_global[i]:
            continue

        chain = []
        curr = i
        visited_local = set()

        while True:
            chain.append(curr)
            visited_local.add(curr)
            visited_global[curr] = True

            nxt = div_sum[curr]

            if nxt > limit or nxt == 0:
                break

            if nxt in visited_local:
                try:
                    idx = chain.index(nxt)
                    cycle = chain[idx:]
                    length = len(cycle)

                    if length > max_len:
                        max_len = length
                        min_elem = min(cycle)
                except ValueError:
                    pass
                break

            if visited_global[nxt]:
                break

            curr = nxt

    return min_elem


if __name__ == "__main__":
    print(solve())
