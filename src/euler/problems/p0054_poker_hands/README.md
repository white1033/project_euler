# Poker Hands

## Problem Statement

The file, `poker.txt`, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

## Solution Analysis

The core of this problem is efficiently comparing two poker hands. Instead of writing deeply nested `if-else` statements to handle every tie-breaking scenario, we can map each hand to a comparable data structure.

### The "Tuple Scoring" Strategy

Python tuples are compared element-by-element from left to right. This behavior perfectly mimics poker hand ranking rules (Category -> Primary Rank -> Secondary Rank -> Kickers).

We convert each hand into a tuple:
```python
(Hand_Category, Primary_Rank, Secondary_Rank, Kicker_1, Kicker_2, ...)
```

#### Hand Categories (Highest to Lowest)
8.  **Straight Flush**: `(8, High_Card)`
7.  **Four of a Kind**: `(7, Quad_Rank, Kicker)`
6.  **Full House**: `(6, Trip_Rank, Pair_Rank)`
5.  **Flush**: `(5, Card1, Card2, Card3, Card4, Card5)` (Sorted High to Low)
4.  **Straight**: `(4, High_Card)`
3.  **Three of a Kind**: `(3, Trip_Rank, Kicker1, Kicker2)`
2.  **Two Pairs**: `(2, High_Pair, Low_Pair, Kicker)`
1.  **One Pair**: `(1, Pair_Rank, Kicker1, Kicker2, Kicker3)`
0.  **High Card**: `(0, Card1, Card2, Card3, Card4, Card5)`

#### Example
Consider **Player 1**: `4D 6S 9H QH QC` (Pair of Queens, 9 kicker)
*   Category: Pair (1)
*   Primary Rank: Q (12)
*   Kickers: 9, 6, 4
*   **Tuple**: `(1, 12, 9, 6, 4)`

Consider **Player 2**: `3D 6D 7H QD QS` (Pair of Queens, 7 kicker)
*   Category: Pair (1)
*   Primary Rank: Q (12)
*   Kickers: 7, 6, 3
*   **Tuple**: `(1, 12, 7, 6, 3)`

**Comparison**:
1.  Compare Category: `1 == 1` (Tie)
2.  Compare Primary: `12 == 12` (Tie)
3.  Compare 1st Kicker: `9 > 7` -> **Player 1 Wins!**

This approach simplifies the logic significantly, as Python handles the lexicographical comparison automatically.