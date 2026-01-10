import csv
import os
from collections import defaultdict

from euler.utils.common import timeit


@timeit
def solve() -> int:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "words.txt")

    with open(file_path) as f:
        reader = csv.reader(f)
        words = next(reader)

    anagrams = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        anagrams[key].append(w)

    pairs = []
    for _key, word_list in anagrams.items():
        if len(word_list) >= 2:
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    pairs.append((word_list[i], word_list[j]))

    max_len = 0
    for w1, _w2 in pairs:
        max_len = max(max_len, len(w1))

    squares_by_len = defaultdict(list)
    k = 1
    while True:
        sq = k * k
        s_sq = str(sq)
        length = len(s_sq)
        if length > max_len:
            break
        squares_by_len[length].append(s_sq)
        k += 1

    max_square = 0

    for w1, w2 in pairs:
        length = len(w1)
        candidates = squares_by_len[length]
        candidates_set = set(candidates)

        for sq_str in candidates:
            mapping = {}
            used_digits = set()
            valid = True

            for char, digit in zip(w1, sq_str, strict=True):
                if char in mapping:
                    if mapping[char] != digit:
                        valid = False
                        break
                else:
                    if digit in used_digits:
                        valid = False
                        break
                    mapping[char] = digit
                    used_digits.add(digit)

            if not valid:
                continue

            if mapping[w2[0]] == "0":
                continue

            w2_num_str = "".join(mapping[c] for c in w2)

            if w2_num_str in candidates_set:
                val1 = int(sq_str)
                val2 = int(w2_num_str)
                max_square = max(max_square, val1, val2)

    return max_square


if __name__ == "__main__":
    print(solve())
