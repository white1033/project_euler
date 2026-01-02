# Lattice Paths

## Problem Statement

Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

(Diagram omitted)

How many such routes are there through a $20 \times 20$ grid?

## Analysis

This is a classic combinatorial problem.

1.  To get from $(0,0)$ to $(n, n)$ in an $n \times n$ grid, we must make exactly $n$ moves to the **Right (R)** and $n$ moves **Down (D)**.
2.  The total number of steps is $n + n = 2n$.
3.  Any valid path is a sequence of length $2n$ containing exactly $n$ **R**'s and $n$ **D**'s.
4.  The number of such sequences is the number of ways to choose the positions of the $n$ **R**'s (or **D**'s) from the $2n$ total positions.

### Formula
The number of paths is given by the binomial coefficient:
$$ \text{Paths} = \binom{2n}{n} = \frac{(2n)!}{n!n!} $$

For $n=20$:
$$ \text{Paths} = \binom{40}{20} $$

### Complexity
Using a direct factorial calculation or `math.comb`:
*   Time Complexity: $O(n)$ or $O(1)$ depending on implementation.
*   Space Complexity: $O(1)$.