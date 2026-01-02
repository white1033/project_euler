# Quadratic Primes

## Problem Statement

Euler discovered the remarkable quadratic formula:
$$ n^2 + n + 41 $$
It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$.

The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.

Considering quadratics of the form:
$$ n^2 + an + b, \text{ where } |a| < 1000 \text{ and } |b| \le 1000 $$

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

## Analysis

### Constraints on $b$
When $n = 0$, the expression becomes $0^2 + a(0) + b = b$.
For the sequence to start with a prime (at $n=0$), **$b$ must be a prime number**.
Given $|b| \le 1000$, we only need to check prime values of $b$ in $[2, 1000]$.

### Constraints on $a$
We iterate $a$ from $-999$ to $999$.
For each pair $(a, b)$, we iterate $n = 0, 1, 2, \dots$ until the value is no longer prime.

### Optimization
*   Precompute primes up to a reasonable limit (e.g., 20,000) for fast $O(1)$ primality testing.
*   Since the max $n$ is likely around 80 (based on the example), the max value is roughly $80^2 + 1000(80) + 1000 \approx 87400$. We can size our sieve accordingly, or use a fallback primality test for larger numbers.

### Complexity
*   Number of $b$: 168 (primes under 1000).
*   Number of $a$: 1999.
*   Total combinations: $168 \times 1999 \approx 3.3 \times 10^5$.
*   For each combination, the loop runs for 'sequence length' times. The average length is very small.
*   Total operations are well within limits ($< 1$ second).