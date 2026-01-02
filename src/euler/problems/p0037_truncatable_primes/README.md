# Problem 37: Truncatable Primes

## Problem Description

The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797, 797, 97,$ and $7$. Similarly we can work from right to left: $3797, 379, 37,$ and $3$.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: $2, 3, 5,$ and $7$ are not considered to be truncatable primes.

## Analysis

We need to find primes that are both **Left-Truncatable** and **Right-Truncatable**.

### Definitions
1.  **Right-Truncatable Prime (RTP)**: Removing digits from the right leaves a prime (e.g., $3797 \to 379 \to 37 \to 3$).
    *   This implies that every prefix of the number is prime.
    *   Example: For $3797$ to be RTP, $3, 37, 379, 3797$ must all be prime.

2.  **Left-Truncatable Prime (LTP)**: Removing digits from the left leaves a prime (e.g., $3797 \to 797 \to 97 \to 7$).
    *   This implies that every suffix of the number is prime.

### Search Strategy: Constructive Approach

Instead of checking all integers up to some arbitrary limit, we can **generate** the candidates. The Right-Truncatable property is perfect for generating candidates tree-style.

#### 1. Generating Right-Truncatable Primes
We can build these digit by digit from left to right.
*   **Start (Single Digit)**: Must be prime.
    *   Roots: $\{2, 3, 5, 7\}$
*   **Extension (Next Digit)**: Append a digit $d$ to a current RTP $P$ to form $P' = P \times 10 + d$.
    *   $P'$ must be prime.
    *   For $P' > 10$, the last digit $d$ cannot be even ($0, 2, 4, 6, 8$) or $5$, otherwise $P'$ is divisible by 2 or 5.
    *   Therefore, $d \in \{1, 3, 7, 9\}$.

We can use a BFS (Breadth-First Search) or Queue to generate these.
1.  Queue = $[2, 3, 5, 7]$
2.  Pop $p$, try appending $d \in \{1, 3, 7, 9\}$.
3.  If $p \times 10 + d$ is prime, add it to Queue.
4.  Repeat until Queue is empty (the tree naturally terminates as primes become sparse).

#### 2. Filtering for Left-Truncatable Primes
For every valid Right-Truncatable Prime generated (except the single digits 2, 3, 5, 7 which are excluded by the problem note), we check if it is also Left-Truncatable.
*   Check if removing the first digit leaves a prime, repeat until single digit.

### Why this works efficiently
This method explores the minimum necessary search space. We don't need to know the upper bound (though it turns out the largest is 739397). The "Truncatable" constraint is very strong, so the number of candidates is small.

## Solution

The solution uses a queue to generate Right-Truncatable Primes and filters them for the Left-Truncatable property.