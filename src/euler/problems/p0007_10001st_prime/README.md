# 10 001st Prime

## Problem Statement

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

## Analysis

To find the $n$-th prime number, we can generate prime numbers in order until we reach the count of $n$.

### Estimation of the $n$-th Prime
The Prime Number Theorem states that the distribution of primes approaches $x / \ln(x)$. The $n$-th prime number $p_n$ is approximately $n \ln n$.

A more precise upper bound for $n \ge 6$ is given by Rosser's Theorem:
$$p_n < n(\ln n + \ln \ln n)$$

For $n = 10,001$:
*   $\ln(10001) \approx 9.21$
*   $\ln(\ln(10001)) \approx \ln(9.21) \approx 2.22$
*   Bound $\approx 10001 \times (9.21 + 2.22) \approx 10001 \times 11.43 \approx 114,311$

Therefore, generating primes up to 120,000 (or 150,000 to be safe) using a **Sieve of Eratosthenes** is an efficient way to find the answer.

### Algorithm
1.  Set a limit $L = 150,000$.
2.  Run Sieve of Eratosthenes up to $L$.
3.  Check if we found at least 10,001 primes.
4.  Return the prime at index 10,000 (0-indexed).