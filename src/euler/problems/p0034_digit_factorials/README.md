# Digit Factorials

## Problem Statement

$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.

## Analysis

We need to find numbers $n$ such that $n$ equals the sum of the factorials of its digits.

### Upper Bound Estimation
Let $f(d) = d!$. We want to find the max $n$.
$9! = 362,880$.
*   A 7-digit number can have a maximum digit factorial sum of $7 \times 9! = 7 \times 362,880 = 2,540,160$.
*   The smallest 8-digit number is $10,000,000$.
*   Since $2,540,160 < 10,000,000$, no 8-digit number (or larger) can satisfy the condition.
*   Therefore, we only need to check up to $2,540,160$.

### Algorithm
1.  Precompute factorials for digits $0-9$.
2.  Iterate $n$ from 3 to $2,540,160$.
3.  For each $n$, sum the factorials of its digits.
4.  If the sum equals $n$, add to the total.

### Complexity
*   **Time Complexity**: $O(N \log_{10} N)$, where $N$ is the upper bound.
*   **Space Complexity**: $O(1)$.