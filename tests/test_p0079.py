from euler.problems.p0079_passcode_derivation.solution import derive_passcode, solve


def test_p0079_simple_derivation():
    # Simulate a small example
    # 1 -> 2 -> 3
    #      2 -> 3 -> 4
    # Expected: 1234
    logs = ["123", "234"]
    assert derive_passcode(logs) == "1234"


def test_p0079_branching():
    # 1 -> 3
    # 2 -> 3
    # 3 -> 4
    # Expected: 1234 or 2134. Our topo sort needs to be stable or just return one valid.
    # But usually topological sort isn't unique.
    # However, for the problem, we assume there's a unique "shortest" path, or we just find one.
    # In this case 1234 and 2134 are both length 4.
    logs = ["134", "234"]
    result = derive_passcode(logs)
    assert result in ["1234", "2134"]


def test_p0079_solution():
    result = solve()
    print(f"\nSolution for Problem 79: {result}")
    assert result is not None
