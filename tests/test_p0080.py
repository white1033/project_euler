from euler.problems.p0080_square_root_digital_expansion.solution import calculate_digital_sum, solve


def test_sqrt_2_digital_sum():
    # Example from problem:
    # The digital sum of the first one hundred decimal digits of sqrt(2) is 475.
    assert calculate_digital_sum(2, 100) == 475


def test_perfect_square():
    # sqrt(4) = 2. It's rational, but if we forced the calculation...
    # The problem asks to sum for irrational roots.
    # Our helper calculate_digital_sum might just calculate digits.
    # sqrt(4) = 2.000... -> sum is 2?
    # Actually, the problem says "irrational square roots", implying we skip integers.
    # But let's check what our helper does for 4.
    # sqrt(4 * 10^200) = 2 * 10^100.
    # The string would be "200000..."
    # The first 100 digits would be '2' then 99 '0's. Sum = 2.
    # This seems consistent.
    assert calculate_digital_sum(4, 100) == 2


def test_p0080_solution():
    result = solve()
    print(f"\nSolution for Problem 80: {result}")
    assert result > 0
