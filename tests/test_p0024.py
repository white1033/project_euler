from euler.problems.p0024_lexicographic_permutations.solution import solve

def test_p0024_example():
    digits = [0, 1, 2]
    assert solve(nth=1, digits=digits) == "012"
    assert solve(nth=2, digits=digits) == "021"
    assert solve(nth=3, digits=digits) == "102"
    assert solve(nth=4, digits=digits) == "120"
    assert solve(nth=5, digits=digits) == "201"
    assert solve(nth=6, digits=digits) == "210" 

def test_p0024_solution():
    assert solve() == "2783915460"
