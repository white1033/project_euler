# Right Triangles with Integer Coordinates

## Problem 91

The points $P(x_1, y_1)$ and $Q(x_2, y_2)$ are plotted at integer coordinates and are joined to the origin, $O(0,0)$, to form $\triangle OPQ$.

There are exactly fourteen triangles containing a right angle that can be formed when each coordinate lies between $0$ and $2$ inclusive; that is, $0 \le x_1, y_1, x_2, y_2 \le 2$.

Given that $0 \le x_1, y_1, x_2, y_2 \le 50$, how many right triangles can be formed?

## Analysis

### Brute Force Approach
The constraints are small: coordinates up to 50.
Total number of points (excluding origin) is $51 \times 51 - 1 = 2600$.
We need to form triangles $\triangle OPQ$. Since order of $P$ and $Q$ doesn't matter (triangle $OPQ$ is same as $OQP$), we look for unique pairs $\{P, Q\}$.
Total pairs: $\binom{2600}{2} \approx 3.38 \times 10^6$.
For each pair, we calculate the squared lengths of the three sides:
- $d_{OP}^2 = x_1^2 + y_1^2$
- $d_{OQ}^2 = x_2^2 + y_2^2$
- $d_{PQ}^2 = (x_1-x_2)^2 + (y_1-y_2)^2$

Then we check Pythagoras' theorem:
- Right angle at $O$: $d_{OP}^2 + d_{OQ}^2 = d_{PQ}^2$
- Right angle at $P$: $d_{OP}^2 + d_{PQ}^2 = d_{OQ}^2$
- Right angle at $Q$: $d_{OQ}^2 + d_{PQ}^2 = d_{OP}^2$

This approach is $O(N^4)$ where $N$ is the grid size. For $N=50$, operations $\approx 3 \times 10^6$ is trivial for Python (< 1 second).

### Optimized Approach
We can count triangles by the location of the right angle.
1.  **Right angle at $O(0,0)$**:
    $P$ must be on x-axis ($x_1, 0$) and $Q$ on y-axis ($0, y_2$).
    There are $N$ choices for $P$ and $N$ choices for $Q$. Total: $N^2$.
    
2.  **Right angle at $P$** (and similarly at $Q$):
    For a fixed $P(x_1, y_1)$ (not on axes), we need $OP \perp PQ$.
    Slope of $OP$ is $m = y_1/x_1$.
    Slope of $PQ$ must be $-1/m = -x_1/y_1$.
    So from $P$, we move by steps of vector $(y_1, -x_1)$ (or simplified by GCD).
    Let $g = \gcd(x_1, y_1)$. Steps are $dx = y_1/g, dy = -x_1/g$.
    We count how many steps we can take in both directions while staying within $[0, N] \times [0, N]$.
    Since symmetry applies, we calculate for $P$ and multiply by 2 (for the case of right angle at $Q$).
    Also need to add cases where $P$ is on axes but $PQ$ is perpendicular (vertical/horizontal segments).
    Specifically:
    - If $P$ is on x-axis ($x_1, 0$), $PQ$ must be vertical ($x_2=x_1, y_2 > 0$). $N$ choices. Total $N^2$ such triangles.
    - If $P$ is on y-axis ($0, y_1$), $PQ$ must be horizontal. $N^2$ such triangles.
    
    Summing these up gives the closed form or optimized count.
    
However, the brute force approach is implemented here for simplicity and verification.
