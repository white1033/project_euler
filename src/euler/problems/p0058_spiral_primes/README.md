# Spiral Primes

## Problem Statement

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

```text
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
```

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of $8/13 \approx 62\%$.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

## Solution Analysis

### Pattern of Diagonal Numbers
This problem is an extension of Problem 28.
For a square spiral of side length $s$ (where $s$ is an odd number):
1.  The square grows in layers. The center is $s=1$. The first layer is $s=3$, the second is $s=5$, etc.
2.  The number of terms on the diagonals for side length $s$ is $2s - 1$.
    *   $s=1$: 1 term (1)
    *   $s=3$: 5 terms (1, 3, 5, 7, 9)
    *   $s=5$: 9 terms
    *   In general, each new layer adds 4 new corners. Total count increases by 4.

### Corner Values
Let the side length be $s$. The step size to get from one corner to the previous corner in the same layer is $s-1$.
The bottom-right corner is always $s^2$.
The other three corners are:
*   Bottom-Left: $s^2 - (s-1)$
*   Top-Left: $s^2 - 2(s-1)$
*   Top-Right: $s^2 - 3(s-1)$

### Optimization
*   The bottom-right corner is $s^2$. Since $s > 1$, $s^2$ is a perfect square and thus **never prime**. We can skip checking this corner.
*   We only need to check the primality of the other three corners.
*   We can maintain a running count of primes (`prime_count`) and total diagonal numbers (`total_count`).

### Algorithm
1.  Initialize `s = 1`, `prime_count = 0`, `total_count = 1`.
2.  Loop indefinitely:
    *   Increase $s$ by 2.
    *   Calculate the three corners of interest:
        *   $c_1 = s^2 - (s-1)$
        *   $c_2 = s^2 - 2(s-1)$
        *   $c_3 = s^2 - 3(s-1)$
    *   Check if $c_1, c_2, c_3$ are prime. Add to `prime_count` if they are.
    *   Increase `total_count` by 4.
    *   Check ratio: if `prime_count / total_count < 0.10`, return $s$.