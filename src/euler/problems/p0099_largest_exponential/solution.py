from euler.utils.common import timeit
import os
from math import log


@timeit
def solve() -> int:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "base_exp.txt")

    max_val = 0
    max_line = 0

    with open(file_path, "r") as f:
        for i, line in enumerate(f, 1):
            if not line.strip():
                continue
            base, exp = map(int, line.strip().split(","))
            val = exp * log(base)

            if val > max_val:
                max_val = val
                max_line = i

    return max_line


if __name__ == "__main__":
    print(solve())
