# Problem 67: Maximum Path Sum II

## Description
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

$$
\mathbf{3}\\
\mathbf{7} \quad 4\\
2 \quad \mathbf{4} \quad 6\\
8 \quad 5 \quad \mathbf{9} \quad 3
$$

That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom in `triangle.txt` (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

**NOTE:** This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are $2^{99}$ altogether! If you could check one trillion ($10^{12}$) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

## Analysis

This problem is computationally identical to **Problem 18**, but with a much larger dataset ($100$ rows).

The brute-force approach would check $2^{N-1}$ paths, where $N=100$, which is $2^{99} \approx 6.3 \times 10^{29}$. This is impossible to compute.

However, using **Dynamic Programming** (specifically a bottom-up approach), we can solve it in $O(N^2)$ time, roughly equal to the number of elements in the triangle.

### Algorithm (Bottom-Up)

We collapse the triangle from the bottom up. For each number, we add the maximum of its two children to itself.

Let $T[r][c]$ be the number at row $r$ and column $c$.
We update $T[r][c]$ as:
$$
T[r][c] \leftarrow T[r][c] + \max(T[r+1][c], T[r+1][c+1])
$$

We iterate $r$ from the second-to-last row up to 0. The final answer is stored in $T[0][0]$.

## Implementation

We read the triangle data from `triangle.txt` into a 2D list and apply the logic described above.
