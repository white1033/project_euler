# Summation of Primes

## Problem Statement

The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.

Find the sum of all the primes below two million.

## Analysis

We need to generate all prime numbers less than $N = 2,000,000$ and sum them up.

### Algorithm
The most efficient way to generate primes up to a specific limit is the **Sieve of Eratosthenes**.

1.  Create a boolean array `is_prime` of size $N$, initialized to `True`.
2.  Mark `is_prime[0]` and `is_prime[1]` as `False`.
3.  Iterate $i$ from 2 to $\sqrt{N}$:
    *   If `is_prime[i]` is `True`, mark all multiples of $i$ (starting from $i^2$) as `False`.
4.  Sum all indices $i$ where `is_prime[i]` is `True`.

### Complexity
*   **Time Complexity**: $O(N \log \log N)$ for the Sieve.
*   **Space Complexity**: $O(N)$ for the array.

For $N = 2 \times 10^6$, this is extremely fast (fraction of a second).