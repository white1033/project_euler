
from euler.utils.common import timeit


@timeit
def solve() -> int:
    limit = 12000
    max_k = 2 * limit

    # min_product_sum[k] stores the minimum N for a set of size k
    min_product_sum = [float("inf")] * (limit + 1)

    def get_min_product_sum(product, current_sum, count, start):
        k = product - current_sum + count

        if k <= limit:
            if product < min_product_sum[k]:
                min_product_sum[k] = product

            for i in range(start, (max_k // product) + 1):
                get_min_product_sum(product * i, current_sum + i, count + 1, i)

    get_min_product_sum(1, 1, 1, 2)

    unique_numbers = set()
    for x in min_product_sum[2:]:
        if x != float("inf"):
            unique_numbers.add(int(x))

    return sum(unique_numbers)


if __name__ == "__main__":
    print(solve())
