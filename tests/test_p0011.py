from euler.problems.p0011_largest_product_in_a_grid.solution import solve

def test_p0011_solution():
    # We don't have a small example in the problem description other than the "marked in red" numbers
    # which gives 1788696. We could verify that our code finds at least that.
    # But for the final answer, we just run it.
    assert solve() == 70600674
