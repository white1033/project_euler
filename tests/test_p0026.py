from euler.problems.p0026_reciprocal_cycles.solution import get_cycle_length, solve


def test_p0026_examples():
    # 1/6 = 0.1(6) -> length 1
    assert get_cycle_length(6) == 1
    # 1/7 = 0.(142857) -> length 6
    assert get_cycle_length(7) == 6
    # 1/2 = 0.5 -> length 0
    assert get_cycle_length(2) == 0

def test_p0026_solution():
    assert solve() == 983
