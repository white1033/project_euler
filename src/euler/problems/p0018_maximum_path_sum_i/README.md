# Maximum Path Sum I

## Problem Statement

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

```text
   3
  7 4
 2 4 6
8 5 9 3
```

That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom of the triangle provided in the problem (15 rows).

## Analysis

### Brute Force vs. Dynamic Programming
The triangle has 15 rows.
*   The top row has 1 number.
*   The second has 2.
*   The $n$-th has $n$.

A brute force approach would explore every possible path. Since each step involves a choice (left-down or right-down), there are $2^{14} = 16,384$ paths. This is small enough for modern computers.

However, **Problem 67** presents the same challenge with 100 rows. $2^{99}$ is approximately $6 \times 10^{29}$, which is impossible to brute force.

### Efficient Algorithm (Bottom-Up DP)
We can solve this efficiently by working from the **bottom up**.

Let $dp[r][c]$ be the maximum path sum starting from row $r$, column $c$ to the bottom.
The recurrence relation is:
$$ dp[r][c] = \text{triangle}[r][c] + \max(dp[r+1][c], dp[r+1][c+1]) $$

Base case: For the last row, the maximum path is simply the value of the cell itself.

We can perform this calculation in-place (or using a single row buffer).
Starting from the second-to-last row, for each number, add the maximum of the two numbers directly below it. Repeat this process until we reach the top.

**Example Trace:**
```
   3
  7 4
 2 4 6
8 5 9 3
```

**Step 1 (Row 2):**
*   `2` becomes `2 + max(8, 5) = 10`
*   `4` becomes `4 + max(5, 9) = 13`
*   `6` becomes `6 + max(9, 3) = 15`
Triangle:
```
   3
  7 4
10 13 15
```

**Step 2 (Row 1):**
*   `7` becomes `7 + max(10, 13) = 20`
*   `4` becomes `4 + max(13, 15) = 19`
Triangle:
```
   3
 20 19
```

**Step 3 (Row 0):**
*   `3` becomes `3 + max(20, 19) = 23`

The result is 23.

### Complexity
*   **Time Complexity**: $O(N)$, where $N$ is the total number of elements in the triangle ($N \approx \frac{R^2}{2}$ for $R$ rows).
*   **Space Complexity**: $O(N)$ to store the triangle (or $O(R)$ if we optimize to use just one row for DP).