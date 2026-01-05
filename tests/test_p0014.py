from euler.problems.p0014_longest_collatz_sequence.solution import solve


def test_p0014_example():
    # We can't easily test the "max under 1,000,000" with a small example,
    # but we can verify our chain logic if we exposed the helper.
    # Since we didn't expose the helper, we can test with a smaller limit if the function supports it.
    # The solve function accepts a limit.
    # Under 14, the longest chain is 9 -> ... (length 20).
    # 13 has length 10.
    # 9: 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, ... (9 + 10 = 19 terms + 1 = 20 terms)
    # Actually let's check:
    # 13 -> 10 terms.
    # 9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 (10 steps to 13) -> ... (9 more steps to 1) => 20 terms.
    assert solve(limit=14) == 9

def test_p0014_solution():
    assert solve() == 837799
