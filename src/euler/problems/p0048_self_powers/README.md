# Problem 48: Self powers

## Problem Description

The series, $1^1 + 2^2 + 3^3 + \dots + 10^{10} = 10405071317$.

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \dots + 1000^{1000}$.

## Analysis

We need to compute:
$$S = \sum_{i=1}^{1000} i^i \pmod{10^{10}}$$

### Modular Arithmetic
The problem asks for the last 10 digits, which is equivalent to finding the sum modulo $10^{10}$.

Properties of modular arithmetic:
1.  $(a + b) \pmod m = ((a \pmod m) + (b \pmod m)) \pmod m$
2.  $(a \times b) \pmod m = ((a \pmod m) \times (b \pmod m)) \pmod m$
3.  $a^b \pmod m$ can be computed efficiently using Modular Exponentiation.

### Python Implementation
Python's built-in `pow(base, exp, mod)` function implements modular exponentiation efficiently.
We simply iterate from 1 to 1000, compute $i^i \pmod{10^{10}}$, and sum them up, taking the modulo at each step (or at the end, since Python handles large integers automatically, but doing it at each step keeps numbers small).

### Complexity
*   **Time Complexity**: $O(N \log N)$ where $N=1000$. The $\log N$ comes from the exponentiation.
*   **Space Complexity**: $O(1)$.

## Solution

The solution iterates through the series and sums the terms modulo $10^{10}$.