# Problem 83: Path Sum: Four Ways

## Description
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in red and bold and is equal to 2297.

$$
\begin{pmatrix}
\color{red}{131} & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18} \\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & \color{red}{150} \\
630 & 803 & 746 & \color{red}{422} & \color{red}{111} \\
537 & 699 & 497 & \color{red}{121} & 956 \\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt, a 31K text file containing an 80 by 80 matrix.

[Link to Problem](https://projecteuler.net/problem=83)

## Analysis

This problem extends Problem 81 and 82 by allowing movement in all four cardinal directions (Left, Right, Up, Down).

### Graph Modeling
Since we can move in any direction (potentially backtracking to find a cheaper route), this cannot be solved with simple one-pass Dynamic Programming like Problem 81 or column-wise DP like Problem 82.

We model this as a **Shortest Path Problem** on a weighted directed graph:
*   **Nodes**: Each cell $(i, j)$ in the matrix.
*   **Edges**: Directed edges from each cell to its 4 neighbors (up, down, left, right).
*   **Weights**: The weight of an edge entering cell $(r, c)$ is the value of the matrix at $(r, c)$. Or more simply, the "cost" of a node is its value.

### Algorithm: Dijkstra
Since all weights (matrix values) are positive integers, **Dijkstra's Algorithm** is the optimal choice.

1.  **Priority Queue (PQ)**: Stores tuples of `(current_path_cost, row, col)`, ordered by cost.
2.  **Distance Matrix**: `min_dist[row][col]` stores the minimum cost found so far to reach cell $(row, col)$. Initialized to $\infty$.
3.  **Initialization**:
    *   Push `(matrix[0][0], 0, 0)` to PQ.
    *   Set `min_dist[0][0] = matrix[0][0]`.
4.  **Iteration**:
    *   Pop the node with the smallest cost from PQ.
    *   If this cost is greater than `min_dist[row][col]`, skip it (outdated path).
    *   If we reached the target $(79, 79)$, return the cost.
    *   Explore neighbors. For each valid neighbor $(nr, nc)$:
        *   `new_cost = current_cost + matrix[nr][nc]`
        *   If `new_cost < min_dist[nr][nc]`:
            *   Update `min_dist`
            *   Push `(new_cost, nr, nc)` to PQ.

### Complexity
*   **Time Complexity**: $O(E \log V)$.
    *   $V = N^2 = 80^2 = 6400$ vertices.
    *   $E \approx 4V$ edges.
    *   With $V=6400$, this is extremely fast.
*   **Space Complexity**: $O(V)$ to store the distance matrix and priority queue.

## Implementation
We use Python's `heapq` module for the priority queue. The matrix is the same 80x80 matrix used in Problem 81 and 82.
