# Number Spiral Diagonals

## Problem Statement

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

```text
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
```

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

## Analysis

We don't need to construct the spiral. We can observe the pattern of the numbers on the diagonals.

Consider an $n \times n$ square (where $n$ is odd).
The top-right corner is always $n^2$.
Since we are moving in a spiral, the other corners can be derived by subtracting $(n-1)$ sequentially.

*   **Top Right**: $n^2$
*   **Top Left**: $n^2 - (n-1)$
*   **Bottom Left**: $n^2 - 2(n-1)$
*   **Bottom Right**: $n^2 - 3(n-1)$

Sum of the 4 corners for layer $n$:
$$ 4n^2 - 6(n-1) = 4n^2 - 6n + 6 $$

### Algorithm
1.  Initialize `total_sum = 1` (the center).
2.  Loop $n$ from 3 to 1001 with step 2.
3.  Add $4n^2 - 6n + 6$ to `total_sum`.

### Complexity
*   **Time Complexity**: $O(N)$, where $N$ is the side length (specifically $N/2$ iterations).
*   **Space Complexity**: $O(1)$.