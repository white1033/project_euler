# Problem 78: Coin Partitions

## Problem Description

Let $p(n)$ represent the number of different ways in which $n$ coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so $p(5)=7$.

Find the least value of $n$ for which $p(n)$ is divisible by one million.

[Link to Problem](https://projecteuler.net/problem=78)

## Analysis

This is a classic partition problem seeking the value of the partition function $p(n)$.
The standard recurrence relation for partitions is given by **Euler's Pentagonal Number Theorem**:

$$ p(n) = \sum_{k \neq 0} (-1)^{k-1} p(n - g_k) $$

where $g_k = \frac{k(3k-1)}{2}$ are the generalized pentagonal numbers for $k = 1, -1, 2, -2, 3, -3, \dots$.

Expanding the series:
$$ p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - \dots $$

The signs follow the pattern: $+, +, -, -, +, +, -, -, \dots$ (two positives, then two negatives).
The indices to subtract are the generalized pentagonal numbers: $1, 2, 5, 7, 12, 15, \dots$.

### Modulo Arithmetic
Since we are only interested in divisibility by $1,000,000$, we perform all calculations modulo $1,000,000$. This prevents the numbers from becoming astronomically large and keeps the arithmetic operations fast.

### Complexity
Using this recurrence, calculating $p(n)$ requires iterating through $k$ such that $g_k \le n$. The number of terms is approximately $\sqrt{2n/3}$, i.e., $O(\sqrt{n})$.
To find the answer $N$, we iterate from $n=1$ upwards. The total time complexity is roughly $\sum_{i=1}^{N} \sqrt{i} \approx O(N^{1.5})$.

## Implementation

We maintain a list `p` storing partition values modulo $1,000,000$. We iterate $n$ starting from 1 and calculate $p(n)$ using the cached values. We stop when $p(n) \equiv 0 \pmod{1000000}$.

```python
def solve(divisor=1000000):
    p = [1]
    n = 1
    while True:
        current_p = 0
        k = 1
        while True:
            # Positive k
            g_k = (k * (3 * k - 1)) // 2
            if g_k > n: break
            sign = 1 if (k % 2 != 0) else -1
            current_p += sign * p[n - g_k]
            
            # Negative k
            g_k_neg = (k * (3 * k + 1)) // 2
            if g_k_neg > n: break
            current_p += sign * p[n - g_k_neg]
            
            k += 1
            
        current_p %= divisor
        if current_p == 0:
            return n
        p.append(current_p)
        n += 1
```
