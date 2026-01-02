# Problem 43: Sub-string Divisibility

## Problem Description

The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.

Let $d_1d_2d_3d_4d_5d_6d_7d_8d_9d_{10}$ be the $10$-digit number. To check divisibility, we use the following triplets:

*   $d_2d_3d_4$ is divisible by $2$
*   $d_3d_4d_5$ is divisible by $3$
*   $d_4d_5d_6$ is divisible by $5$
*   $d_5d_6d_7$ is divisible by $7$
*   $d_6d_7d_8$ is divisible by $11$
*   $d_7d_8d_9$ is divisible by $13$
*   $d_8d_9d_{10}$ is divisible by $17$

Find the sum of all $0$ to $9$ pandigital numbers with this property.

## Analysis

We need to find 10-digit pandigital numbers that satisfy a chain of divisibility rules.

### Brute Force vs. Constructive Approach
Checking all $10! = 3,628,800$ permutations is feasible ($\approx 1-2$ seconds), but we can do much better by **constructing** the number from the constraints.

The constraints overlap:
*   Rule 7: $d_8d_9d_{10}$ divisible by 17.
*   Rule 6: $d_7d_8d_9$ divisible by 13.
*   ...

This suggests a **Backtracking** or **Reverse Search** strategy.

### Algorithm: Reverse Construction

1.  **Start with the last triplet**: Find all 3-digit numbers (with leading zeros allowed, e.g., "017") that are divisible by 17. These form the candidates for $d_8d_9d_{10}$.
2.  **Iterate backwards**:
    *   For the next divisor (13), we look for a digit $d_7$ such that $d_7d_8d_9$ is divisible by 13.
    *   The "tail" $d_8d_9$ is already fixed from the previous step.
    *   We prepend $d_7$ to our candidate string.
    *   **Crucial Step**: Check for duplicate digits immediately. Since the final number must be pandigital, we discard any candidate where $d_7$ is already in $\{d_8, \dots, d_{10}\}$.
3.  **Repeat** for divisors 11, 7, 5, 3, 2.
4.  **Finalize**:
    *   After satisfying all divisibility rules, we have strings $d_2 \dots d_{10}$.
    *   Find the one missing digit to perform $d_1$.
    *   Ensure $d_1 \ne 0$ (no leading zeros for a 10-digit number).
    *   Sum the valid numbers.

### Complexity
The search space is drastically reduced.
*   Multiples of 17: $\approx 1000/17 \approx 58$ candidates.
*   Each step filters these candidates.
*   The number of valid suffixes at each step remains very small (likely $< 100$).
*   Total operations: Negligible ($< 1$ ms).

## Solution

The solution implements the reverse construction strategy, building valid suffixes from right to left.