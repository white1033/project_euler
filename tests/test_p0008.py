from euler.problems.p0008_largest_product_in_a_series.solution import solve


def test_p0008_example():
    # The four adjacent digits in the 1000-digit number that have the greatest product
    # are 9 x 9 x 8 x 9 = 5832
    assert solve(adjacent_digits=4) == 5832


def test_p0008_solution():
    assert solve() == 23514624000
