from euler.utils.common import timeit


@timeit
def solve() -> int:
    """
    Finds the sum of the only ordered set of six cyclic 4-digit numbers for which
    each of the polygonal types: triangle, square, pentagonal, hexagonal, heptagonal,
    and octagonal, is represented by a different number in the set.
    """

    # 1. Generate all 4-digit polygonal numbers for types 3 to 8
    polygonal_numbers: dict[int, list[int]] = {}

    formulas = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2),
    }

    for p_type, formula in formulas.items():
        nums = []
        n = 1
        while True:
            val = formula(n)
            if val >= 10000:
                break
            # If val % 100 < 10, it cannot connect to a 4-digit number (which starts with >= 10).
            if val >= 1000 and val % 100 >= 10:
                nums.append(val)
            n += 1
        polygonal_numbers[p_type] = nums

    # 2. Build a mapping prefix -> list of (number, type)
    candidates_by_start: dict[int, list[tuple[int, int]]] = {}
    for p_type, nums in polygonal_numbers.items():
        for num in nums:
            start = num // 100
            if start not in candidates_by_start:
                candidates_by_start[start] = []
            candidates_by_start[start].append((num, p_type))

    # 3. Backtracking
    result_sum = 0

    def find_cycle(current_chain: list[int], used_types: set[int]):
        nonlocal result_sum
        if result_sum > 0:  # Found it
            return

        last_num = current_chain[-1]
        suffix = last_num % 100

        if len(current_chain) == 6:
            # Check cycle condition back to start
            first_num = current_chain[0]
            prefix_first = first_num // 100
            if suffix == prefix_first:
                # Found the cycle!
                result_sum = sum(current_chain)
            return

        # Find candidates for next number
        if suffix in candidates_by_start:
            possible_nexts = candidates_by_start[suffix]
            for next_num, next_type in possible_nexts:
                if next_type not in used_types and next_num not in current_chain:
                    find_cycle(current_chain + [next_num], used_types | {next_type})

    # Start with type 8
    for num8 in polygonal_numbers[8]:
        find_cycle([num8], {8})
        if result_sum > 0:
            break

    return result_sum


if __name__ == "__main__":
    print(solve())