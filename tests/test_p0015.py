from euler.problems.p0015_lattice_paths.solution import solve


def test_p0015_example():
    # Starting in the top left corner of a 2 x 2 grid... there are exactly 6 routes
    assert solve(grid_size=2) == 6

def test_p0015_solution():
    assert solve() == 137846528820
