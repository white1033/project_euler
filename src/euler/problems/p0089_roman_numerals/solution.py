from euler.utils.common import timeit
import os


def roman_to_int(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_val = 0
    for char in reversed(s):
        val = values[char]
        if val < prev_val:
            total -= val
        else:
            total += val
        prev_val = val
    return total


def int_to_roman(n: int) -> str:
    mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    res = []
    for val, char in mapping:
        count = n // val
        if count > 0:
            res.append(char * count)
            n -= val * count
    return "".join(res)


@timeit
def solve() -> int:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "roman.txt")

    saved_chars = 0

    with open(file_path, "r") as f:
        for line in f:
            original = line.strip()
            if not original:
                continue

            value = roman_to_int(original)
            minimal = int_to_roman(value)

            saved_chars += len(original) - len(minimal)

    return saved_chars


if __name__ == "__main__":
    print(solve())
