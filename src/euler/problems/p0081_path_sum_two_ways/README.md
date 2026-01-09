# Problem 81: Path Sum: Two Ways

## Description
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

$$
\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18 \\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150 \\
630 & 803 & \color{red}{746} & \color{red}{422} & 111 \\
537 & 699 & 497 & \color{red}{121} & 956 \\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt, a 31K text file containing an 80 by 80 matrix.

[Link to Problem](https://projecteuler.net/problem=81)

## Analysis

This is a classic **Dynamic Programming** problem. We need to find the minimum path sum to reach the bottom-right cell $(N-1, N-1)$ from the top-left cell $(0, 0)$.

Let $dp[i][j]$ be the minimal path sum to reach cell $(i, j)$.
Since we can only move **right** and **down**, a cell $(i, j)$ can only be reached from:
1.  **Top**: $(i-1, j)$
2.  **Left**: $(i, j-1)$

Thus, the recurrence relation is:
$$ dp[i][j] = \text{matrix}[i][j] + \min(dp[i-1][j], dp[i][j-1]) $$

### Boundary Conditions
*   **Start**: $dp[0][0] = \text{matrix}[0][0]$
*   **First Row ($i=0$)**: Can only be reached from the left.
    $$ dp[0][j] = dp[0][j-1] + \text{matrix}[0][j] $$
*   **First Column ($j=0$)**: Can only be reached from above.
    $$ dp[i][0] = dp[i-1][0] + \text{matrix}[i][0] $$

### Complexity
*   **Time Complexity**: $O(N \times M)$ where $N$ and $M$ are the dimensions of the matrix. For this problem, $80 \times 80 = 6400$ operations, which is instantaneous.
*   **Space Complexity**: $O(1)$ if we modify the input matrix in-place, or $O(N \times M)$ if we create a separate DP table.

## Implementation

We implement the solution using the in-place approach to save memory. We iterate through the matrix, updating each cell with the cumulative minimal sum.
