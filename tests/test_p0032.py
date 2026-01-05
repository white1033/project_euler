from euler.problems.p0032_pandigital_products.solution import is_pandigital, solve


def test_p0032_example():
    # 39 * 186 = 7254
    # 391867254 is pandigital
    assert is_pandigital("391867254") == True
    
def test_p0032_solution():
    assert solve() == 45228
