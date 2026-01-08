# Problem 77: Prime Summations

## Problem Description

It is possible to write ten as the sum of primes in exactly five different ways:

$$
\begin{align}
&7 + 3 \\
&5 + 5 \\
&5 + 3 + 2 \\
&3 + 3 + 2 + 2 \\
&2 + 2 + 2 + 2 + 2
\end{align}
$$

What is the first value which can be written as the sum of primes in over five thousand different ways?

[Link to Problem](https://projecteuler.net/problem=77)

## Analysis

This problem is very similar to **Problem 76**, but instead of partitioning an integer into any positive integers (excluding the number itself for "at least two"), we are partitioning an integer into **sums of primes**.

This is essentially the **Coin Change Problem** (unbounded knapsack), where the "coins" are the prime numbers $2, 3, 5, 7, \dots$.

Let $ways[i]$ be the number of ways to write integer $i$ as a sum of primes.
Initialize $ways[0] = 1$ (one way to form 0: using no primes).

Iterate through each prime $p$:
  For each $j$ from $p$ to our target limit:
    $ways[j] = ways[j] + ways[j - p]$

Since we don't know the target number $N$ beforehand, we can estimate a limit or search dynamically.
1. Start with a small limit (e.g., 100).
2. Generate primes up to this limit.
3. Compute partition counts using DP.
4. Check if any number $i \le limit$ has $ways[i] > 5000$.
5. If found, return the first such $i$.
6. If not found, double the limit and repeat.

Given the example where 10 has 5 ways, and the target is 5000 ways, the answer is likely not extremely large, so a small initial limit works well.

## Implementation

We use a dynamic limit strategy.

```python
def solve(threshold=5000):
    limit = 10
    while True:
        primes = sieve_of_eratosthenes(limit)
        ways = [0] * (limit + 1)
        ways[0] = 1
        
        for p in primes:
            for j in range(p, limit + 1):
                ways[j] += ways[j - p]
                
        # Check if we found the number
        for i in range(2, limit + 1):
            if ways[i] > threshold:
                return i
                
        limit *= 2
```
