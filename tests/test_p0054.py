import pytest
from euler.problems.p0054_poker_hands.solution import solve, evaluate_hand

def test_evaluate_hand_examples():
    # 1. Pair of 5s vs Pair of 8s
    h1 = "5H 5C 6S 7S KD".split()
    h2 = "2C 3S 8S 8D TD".split()
    assert evaluate_hand(h1) < evaluate_hand(h2)

    # 2. High Ace vs High Queen
    h1 = "5D 8C 9S JS AC".split()
    h2 = "2C 5C 7D 8S QH".split()
    assert evaluate_hand(h1) > evaluate_hand(h2)

    # 3. Three Aces vs Flush
    h1 = "2D 9C AS AH AC".split()
    h2 = "3D 6D 7D TD QD".split()
    assert evaluate_hand(h1) < evaluate_hand(h2) # Flush (5) > Trips (3)

    # 4. Pair Queens (High 9) vs Pair Queens (High 7)
    h1 = "4D 6S 9H QH QC".split()
    h2 = "3D 6D 7H QD QS".split()
    assert evaluate_hand(h1) > evaluate_hand(h2)

    # 5. Full House (4s over ?) vs Full House (3s over ?)
    h1 = "2H 2D 4C 4D 4S".split()
    h2 = "3C 3D 3S 9S 9D".split()
    assert evaluate_hand(h1) > evaluate_hand(h2)

def test_solution_full_dataset():
    """
    Test the final solution using the full poker.txt dataset.
    The correct answer for the full 1000 hands is 376.
    """
    assert solve() == 376
