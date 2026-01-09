import random
from collections import Counter

from euler.utils.common import timeit


def get_next_railway(pos: int) -> int:
    """Returns the index of the next railway station."""
    # Railways are at 5, 15, 25, 35
    if pos < 5 or pos >= 35:
        return 5
    if pos < 15:
        return 15
    if pos < 25:
        return 25
    return 35


def get_next_utility(pos: int) -> int:
    """Returns the index of the next utility company."""
    # Utilities are at 12, 28
    if pos < 12 or pos >= 28:
        return 12
    return 28


@timeit
def solve(dice_sides: int = 4, iterations: int = 1_000_000) -> str:
    """
    Monte Carlo simulation of Monopoly to find the modal string of the 3 most visited squares.
    """
    # Board constants
    GO = 0
    JAIL = 10
    G2J = 30
    CC = {2, 17, 33}
    CH = {7, 22, 36}

    # State
    current_pos = 0
    double_streak = 0

    # Statistics
    visits = Counter()

    # Cards (We don't need to simulate the deck order, random choice is sufficient for long run)
    # Community Chest: 16 cards total. 1 -> GO, 1 -> JAIL, 14 -> No movement
    # Chance: 16 cards total.
    # 1->GO, 1->JAIL, 1->C1, 1->E3, 1->H2, 1->R1, 2->Next R, 1->Next U, 1->Back 3, 6->No mov

    for _ in range(iterations):
        # 1. Roll Dice
        d1 = random.randint(1, dice_sides)
        d2 = random.randint(1, dice_sides)

        # 2. Check Doubles
        if d1 == d2:
            double_streak += 1
        else:
            double_streak = 0

        # 3. Handle Triple Doubles (Speeding)
        if double_streak == 3:
            current_pos = JAIL
            double_streak = 0
            visits[current_pos] += 1
            continue

        # 4. Move
        current_pos = (current_pos + d1 + d2) % 40

        # 5. Handle Special Squares (Recursively? Rule says movement instructions are followed)
        # Note: "Go back 3 squares" from Chance could land on Community Chest.
        # We need to handle this potential chain. A simple while loop or recursive check works.
        # However, the only chain is CH -> Back 3 -> CC? Or CH -> Back 3 -> Land on regular square.
        # Let's just process the position logic once, and if it changes, process again if needed.
        # Actually, the problem implies instantaneous jumps.

        # We process landing events until we settle.
        while True:
            original_pos = current_pos

            # Go To Jail
            if current_pos == G2J:
                current_pos = JAIL

            # Community Chest
            elif current_pos in CC:
                # Pick a card (1/16 prob for each special action)
                card = random.randint(1, 16)
                if card == 1:
                    current_pos = GO
                elif card == 2:
                    current_pos = JAIL
                # Else stay

            # Chance
            elif current_pos in CH:
                card = random.randint(1, 16)
                if card == 1:
                    current_pos = GO
                elif card == 2:
                    current_pos = JAIL
                elif card == 3:
                    current_pos = 11  # C1
                elif card == 4:
                    current_pos = 24  # E3
                elif card == 5:
                    current_pos = 39  # H2
                elif card == 6:
                    current_pos = 5  # R1
                elif card == 7 or card == 8:  # Next R
                    current_pos = get_next_railway(current_pos)
                elif card == 9:  # Next U
                    current_pos = get_next_utility(current_pos)
                elif card == 10:  # Back 3
                    current_pos = (current_pos - 3) % 40

            # If position didn't change, we are done
            if current_pos == original_pos:
                break

        # 6. Record Visit
        visits[current_pos] += 1

    # Find top 3
    most_common = visits.most_common(3)

    # Format result: 6-digit string
    result_str = "".join(f"{square:02d}" for square, _ in most_common)

    return result_str


if __name__ == "__main__":
    # To stabilize results, we might want a fixed seed, but for Monte Carlo large N is better.
    random.seed(42)
    result = solve()
    print(f"Result: {result}")
