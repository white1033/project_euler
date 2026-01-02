# Longest Collatz Sequence

## Problem Statement

The following iterative sequence is defined for the set of positive integers:

*   $n \to n/2$ ($n$ is even)
*   $n \to 3n + 1$ ($n$ is odd)

Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$

It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.

Which starting number, under one million, produces the longest chain?
**NOTE:** Once the chain starts the terms are allowed to go above one million.

## Analysis

We need to find the starting number $n < 1,000,000$ that produces the longest Collatz sequence.

### Algorithm: Memoization (Caching)
Since many sequences merge (e.g., the sequence for 26 becomes the sequence for 13 after one step), we can use **Memoization** to store the length of the sequence for each number we encounter.

1.  Define `length(n)`:
    *   If $n=1$, return 1.
    *   If `length(n)` is cached, return it.
    *   If $n$ is even, `length(n) = 1 + length(n/2)`.
    *   If $n$ is odd, `length(n) = 1 + length(3n+1)`.
    *   Cache and return the result.

2.  Iterate $i$ from 1 to 999,999.
3.  Compute `length(i)` and keep track of the maximum.

### Complexity
This approach is extremely efficient because each number in a chain is processed only once (the first time it is encountered). Subsequent encounters take $O(1)$. The time complexity is roughly proportional to the total number of unique steps across all numbers, which is manageable for $N=10^6$.