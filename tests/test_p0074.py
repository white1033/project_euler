from euler.problems.p0074_digit_factorial_chains.solution import next_number, solve


def test_next_number():
    assert next_number(145) == 145
    assert next_number(169) == 363601
    assert next_number(363601) == 1454
    assert next_number(1454) == 169


def test_p0074_solution():
    result = solve(1000000)
    assert result > 0
    print(f"\nSolution for Problem 74: {result}")
