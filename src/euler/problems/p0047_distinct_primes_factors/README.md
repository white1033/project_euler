# Problem 47: Distinct Primes Factors

## Problem Description

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

## Analysis

We need to find $n$ such that:
*   $\omega(n) = 4$
*   $\omega(n+1) = 4$
*   $\omega(n+2) = 4$
*   $\omega(n+3) = 4$
Where $\omega(x)$ is the number of distinct prime factors of $x$.

### Search Strategy: Sieve Method

Instead of factoring each number individually (which is slow for many numbers), we can use a **Sieve** variant.

1.  Create an array `factors_count` of size $N$ initialized to 0.
2.  Iterate from $i = 2$ to $N$.
3.  If `factors_count[i] == 0`, then $i$ is **prime**.
    *   Iterate through all multiples of $i$: $j = i, 2i, 3i, \dots$ up to $N$.
    *   Increment `factors_count[j]`.
    *   This efficiently counts distinct prime factors for all numbers up to $N$.
4.  After sieving, scan the array for 4 consecutive entries where `factors_count` is 4.

### Complexity
*   **Time Complexity**: $O(N \log \log N)$ (Standard Sieve complexity).
*   **Space Complexity**: $O(N)$ for the array.

Given the constraints (4 factors), the smallest candidate is $2 \times 3 \times 5 \times 7 = 210$. The numbers shouldn't be astronomically large, so a sieve size of 200,000 is a reasonable starting point.

## Solution

The solution implements the prime factor counting sieve and scans for the consecutive sequence.