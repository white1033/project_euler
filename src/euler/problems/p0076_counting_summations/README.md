# Problem 76: Counting Summations

## Problem Description

It is possible to write five as a sum in exactly six different ways:

$$
\begin{align}
&4 + 1 \\
&3 + 2 \\
&3 + 1 + 1 \\
&2 + 2 + 1 \\
&2 + 1 + 1 + 1 \\
&1 + 1 + 1 + 1 + 1
\end{align}
$$

How many different ways can one hundred be written as a sum of at least two positive integers?

[Link to Problem](https://projecteuler.net/problem=76)

## Analysis

This is a classic **Integer Partition** problem. Let $p(n)$ be the number of partitions of an integer $n$.
The problem asks for the number of ways to write $n$ as a sum of *at least two* positive integers, which is equivalent to $p(n) - 1$ (excluding the case where $n$ is written as itself).

### Approach 1: Dynamic Programming

We can view this as an **Unbounded Knapsack Problem** (or Coin Change Problem) where:
- Target sum: $n$
- Items (coins): Integers $1, 2, 3, \dots, n-1$
- We want to find the number of ways to form sum $n$.

Let $ways[i]$ be the number of ways to partition integer $i$ using the available items.
Initialize $ways[0] = 1$.

For each item $k$ from $1$ to $n-1$:
  For each sum $j$ from $k$ to $n$:
    $ways[j] = ways[j] + ways[j - k]$

After iterating through all items up to $n-1$, $ways[n]$ will contain the answer.

**Complexity:**
- Time Complexity: $O(n^2)$
- Space Complexity: $O(n)$

### Approach 2: Generating Functions (Euler's Pentagonal Number Theorem)

The partition function $p(n)$ has the generating function:
$$ \sum_{n=0}^{\infty} p(n)x^n = \prod_{k=1}^{\infty} \frac{1}{1-x^k} $$

By Euler's Pentagonal Number Theorem:
$$ \prod_{k=1}^{\infty} (1-x^k) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2} = 1 - x^1 - x^2 + x^5 + x^7 - x^{12} - x^{15} + \dots $$

This gives us a recurrence relation for $p(n)$:
$$ p(n) = \sum_{k \neq 0, g_k \le n} (-1)^{k-1} p(n - g_k) $$
where $g_k = \frac{k(3k-1)}{2}$ are the generalized pentagonal numbers ($1, 2, 5, 7, 12, 15, \dots$).

The terms are added/subtracted in pairs: $p(n-1) + p(n-2) - p(n-5) - p(n-7) + \dots$

**Complexity:**
- Time Complexity: $O(n \sqrt{n})$ because there are $O(\sqrt{n})$ pentagonal numbers less than $n$.
- Space Complexity: $O(n)$ to store previous partition values.

## Implementation

The solution uses the Dynamic Programming approach as it is very efficient for $N=100$.

```python
def solve(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    # Items from 1 to n-1 to exclude the partition of n itself
    for k in range(1, n):
        for j in range(k, n + 1):
            ways[j] += ways[j - k]
    return ways[n]
```

### Performance Comparison

While the DP approach is sufficient for $N=100$, the Generating Function approach (using Pentagonal Number Theorem) is significantly faster for larger $N$.

Benchmark results for $N=5000$:
- **DP ($O(n^2)$)**: ~0.73 seconds
- **Pentagonal ($O(n\sqrt{n})$)**: ~0.06 seconds

The Pentagonal Number approach is over **10x faster** at this scale.
