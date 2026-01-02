# Digit Fifth Powers

## Problem Statement

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

$$ 1634 = 1^4 + 6^4 + 3^4 + 4^4 $$
$$ 8208 = 8^4 + 2^4 + 0^4 + 8^4 $$
$$ 9474 = 9^4 + 4^4 + 7^4 + 4^4 $$

As $1 = 1^4$ is not a sum it is not included.

The sum of these numbers is $1634 + 8208 + 9474 = 19316$.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

## Analysis

We need to find numbers $n$ such that $n$ equals the sum of the fifth powers of its digits.

### Upper Bound
First, we need to find an upper bound for $n$.
The maximum value for a single digit's fifth power is $9^5 = 59049$.

*   For a 5-digit number, the max sum is $5 \times 9^5 = 295,245$. This is a 6-digit number, so a 5-digit number is possible.
*   For a 6-digit number, the max sum is $6 \times 9^5 = 354,294$. This is still a 6-digit number.
*   For a 7-digit number, the max sum is $7 \times 9^5 = 413,343$. This is a 6-digit number, which is smaller than the smallest 7-digit number ($1,000,000$).

Therefore, no 7-digit number (or larger) can satisfy the condition. The upper bound is $6 \times 9^5 = 354,294$.

### Algorithm
1.  Iterate $n$ from 2 (since 1 is excluded) up to 355,000.
2.  For each $n$, calculate the sum of the fifth powers of its digits.
3.  If the sum equals $n$, add $n$ to the total sum.

### Optimization
We can precompute the fifth powers of digits $0-9$ to avoid repeated exponentiation.
`powers = [d**5 for d in range(10)]`