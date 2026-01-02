# Reciprocal Cycles

## Problem Statement

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
*   $1/2 = 0.5$
*   $1/3 = 0.(3)$
*   $1/4 = 0.25$
*   $1/5 = 0.2$
*   $1/6 = 0.1(6)$
*   $1/7 = 0.(142857)$
*   $1/8 = 0.125$
*   $1/9 = 0.(1)$
*   $1/10 = 0.1$

Where $0.1(6)$ means $0.166666\dots$, and has a 1-digit recurring cycle. It can be seen that $1/7$ has a 6-digit recurring cycle.

Find the value of $d < 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.

## Analysis

We need to find the length of the recurring cycle for $1/d$. This is equivalent to finding the order of 10 modulo $d$ (after removing factors of 2 and 5).

### Method: Long Division Simulation
We can simulate the long division process of $1 \div d$.
1.  Keep track of the `remainder` at each step.
2.  Multiply remainder by 10, calculate new remainder: `remainder = (remainder * 10) % d`.
3.  Store the `position` (index) where each remainder was first seen.
4.  If a remainder repeats, we found a cycle!
    *   `cycle_length = current_position - seen_position[remainder]`
5.  If remainder becomes 0, the decimal terminates (cycle length 0).

### Optimization
*   The maximum possible cycle length for $d$ is $d-1$ (for prime numbers).
*   If we iterate $d$ from 999 down to 2, and we find a cycle of length $L$, we can stop searching if the current $d \le L$, because no smaller number can produce a longer cycle.

### Complexity
*   **Time Complexity**: Roughly $\sum d$. In the worst case (primes), simulation takes $d$ steps. Total roughly $O(N^2)$. For $N=1000$, this is instant.
*   **Space Complexity**: $O(d)$ to store remainders.