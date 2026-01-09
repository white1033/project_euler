# Problem 84: Monopoly Odds

## Description
In the game, **Monopoly**, the standard board is set up in the following way:
(Image omitted)

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

(Rules details omitted for brevity, see code for implementation)

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

[Link to Problem](https://projecteuler.net/problem=84)

## Analysis

This problem asks for the steady-state probability distribution of landing on each square of the Monopoly board using two 4-sided dice.

### Approaches
1.  **Markov Chain**: Construct a transition matrix ($120 \times 120$ states to account for position and consecutive doubles) and find the eigenvector corresponding to eigenvalue 1. This gives the exact probabilities.
2.  **Monte Carlo Simulation**: Simulate a game played for a very large number of turns and count the visits to each square.

Given the complex rules (Chance cards, Community Chest cards, Triple Doubles, Go To Jail), a simulation is often less error-prone to implement than a transition matrix and converges quickly enough for the required precision (ranking the top 3 squares).

### Simulation Details
*   **Dice**: Two 4-sided dice (range 1-4).
*   **Board**: 40 squares (00-39).
*   **Special Rules Implemented**:
    *   **Doubles**: Count consecutive doubles. 3 doubles $\to$ JAIL.
    *   **G2J**: Land on square 30 $\to$ JAIL (10).
    *   **Community Chest (CC)**: Squares 02, 17, 33. 2/16 cards move (GO, JAIL).
    *   **Chance (CH)**: Squares 07, 22, 36. 10/16 cards move (GO, JAIL, C1, E3, H2, R1, Next R x2, Next U, Back 3).
    *   **"Back 3 Squares"**: If moved back from CH to CC, trigger CC logic? (Implied "movement instructions are followed"). Actually, Chance 36 back 3 lands on CC 33. We must handle this chain. The solution iteratively settles the position.

### Results (Two 4-sided dice)
Running the simulation for 1,000,000 turns yields consistent top 3 squares.

Top 3 Squares:
1.  **JAIL (10)**: Due to G2J, CC card, CH card, and Triple Doubles.
2.  **R2 (15)**: Likely due to "Go to next R" cards from CH1 (07).
3.  **E3 (24)**: High traffic area.

Modal String: **101524**

## Complexity
*   **Time Complexity**: $O(N)$ where $N$ is the number of simulation steps.
*   **Space Complexity**: $O(1)$ (fixed board size).
