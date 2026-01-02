from euler.problems.p0017_number_letter_counts.solution import solve, count_letters

def test_p0017_examples():
    # 1 to 5: one, two, three, four, five -> 3+3+5+4+4 = 19
    assert solve(limit=5) == 19
    
    # 342 (three hundred and forty-two) contains 23 letters
    assert count_letters(342) == 23
    
    # 115 (one hundred and fifteen) contains 20 letters
    assert count_letters(115) == 20

def test_p0017_solution():
    assert solve() == 21124
