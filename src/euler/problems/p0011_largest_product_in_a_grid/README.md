# Largest Product in a Grid

## Problem Statement

In the $20 \times 20$ grid below, four numbers along a diagonal line have been marked in red.

(Grid omitted for brevity, see solution source code)

The product of these numbers is $26 \times 63 \times 78 \times 14 = 1788696$.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the $20 \times 20$ grid?

## Analysis

We need to check all possible sequences of 4 adjacent numbers in the grid.
For each cell $(r, c)$, we can check 4 directions starting from that cell:
1.  **Horizontal**: $(r, c), (r, c+1), (r, c+2), (r, c+3)$
2.  **Vertical**: $(r, c), (r+1, c), (r+2, c), (r+3, c)$
3.  **Diagonal (Main)**: $(r, c), (r+1, c+1), (r+2, c+2), (r+3, c+3)$
4.  **Diagonal (Anti)**: $(r, c), (r+1, c-1), (r+2, c-2), (r+3, c-3)$

We iterate through all cells and update the maximum product found so far. Boundary checks are necessary to strictly stay within the $20 \times 20$ grid.

### Complexity
*   Grid size $N \times M$ ($20 \times 20$).
*   Length of sequence $K=4$.
*   Complexity is $O(N \cdot M \cdot K)$, which is roughly $20 \times 20 \times 4$ operations. Very small.