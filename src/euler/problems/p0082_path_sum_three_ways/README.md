# Problem 82: Path Sum: Three Ways

## Description
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

$$
\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18} \\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150 \\
630 & 803 & 746 & 422 & 111 \\
537 & 699 & 497 & 121 & 956 \\
805 & 732 & 524 & 37 & 331
\end{pmatrix}
$$

Find the minimal path sum from the left column to the right column in matrix.txt, a 31K text file containing an 80 by 80 matrix.

[Link to Problem](https://projecteuler.net/problem=82)

## Analysis

This problem is an extension of Problem 81, adding the ability to move **Up**. The allowed moves are **Right**, **Down**, and **Up**. We need to find the minimum path sum from anywhere in the left column to anywhere in the right column.

### Dynamic Programming Approach

Since we can move vertically (up and down) freely within a column but only move **Right** to advance to the next column, we can solve this problem column by column.

Let $dp[i]$ be the minimum cost to reach the cell at row $i$ in the current column being processed.

For the first column (column 0), the cost is simply the value of the matrix cells:
$$ dp[i] = \text{matrix}[i][0] $$

For each subsequent column $j$ (from 1 to $N-1$):

1.  **Initialize from Left**:
    First, we calculate the cost of arriving at each cell $(i, j)$ directly from the left $(i, j-1)$.
    $$ \text{cost}[i] = dp[i] + \text{matrix}[i][j] $$

2.  **Propagate Downwards**:
    Check if it's cheaper to reach cell $(i, j)$ by moving down from $(i-1, j)$.
    $$ \text{cost}[i] = \min(\text{cost}[i], \text{cost}[i-1] + \text{matrix}[i][j]) $$
    We iterate $i$ from $1$ to $N-1$.

3.  **Propagate Upwards**:
    Check if it's cheaper to reach cell $(i, j)$ by moving up from $(i+1, j)$.
    $$ \text{cost}[i] = \min(\text{cost}[i], \text{cost}[i+1] + \text{matrix}[i][j]) $$
    We iterate $i$ from $N-2$ down to $0$.

After processing these three steps for column $j$, $\text{cost}[i]$ holds the true minimum path sum to reach $(i, j)$. We update $dp$ with these new values and proceed to the next column.

Finally, the answer is the minimum value in the $dp$ array after processing the last column.

### Complexity

*   **Time Complexity**: $O(N \times M)$ where $N$ is rows and $M$ is columns. For each column, we perform three passes (initial, down, up), so the constant factor is small. For $80 \times 80$, this is roughly $19,200$ operations.
*   **Space Complexity**: $O(N)$ to store the DP array for the current column.

## Implementation Notes

We reuse the `0081_matrix.txt` file (renamed/copied to `0082_matrix.txt`) as it is the same 80x80 matrix used in Problem 81, 82, and 83.
