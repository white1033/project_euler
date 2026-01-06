# Convergents of e

## Problem Description

The square root of 2 can be written as an infinite continued fraction: $\sqrt{2} = [1; (2)]$.
The constant $e$ is given by $e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2k, 1, \dots]$.

The first ten terms in the sequence of convergents for $e$ are:
$$ 2, 3, \frac{8}{3}, \frac{11}{4}, \frac{19}{7}, \frac{87}{32}, \frac{106}{39}, \frac{193}{71}, \frac{1264}{465}, \frac{1457}{536}, \dots $$

The sum of digits in the numerator of the 10th convergent is $1+4+5+7=17$.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for $e$.

## Mathematical Analysis

### Recurrence Relation for Convergents

For any continued fraction $[a_0; a_1, a_2, \dots]$, the $n$-th convergent (let's index from 0, so the problem's "1st" is index 0) $h_n / k_n$ is given by:

*   $h_n = a_n h_{n-1} + h_{n-2}$
*   $k_n = a_n k_{n-1} + k_{n-2}$

With initial values:
*   $h_{-1} = 1, h_{-2} = 0$
*   $k_{-1} = 0, k_{-2} = 1$

### Coefficient Pattern for $e$

The coefficients $a_k$ for $e$ follow a specific pattern:
*   $a_0 = 2$
*   For $k \ge 1$:
    *   If $k \equiv 2 \pmod 3$, then $a_k = 2 \cdot \frac{k+1}{3}$.
    *   Otherwise, $a_k = 1$.

The sequence looks like:
*   $k=0: 2$
*   $k=1: 1$
*   $k=2: 2$ ($2 \times 1$)
*   $k=3: 1$
*   $k=4: 1$
*   $k=5: 4$ ($2 \times 2$)
*   ...

### Computation

To find the 100th convergent (which corresponds to index $k=99$), we simply iterate this recurrence 100 times. Since we only need the numerator sum, we only track $h_k$. Python handles arbitrarily large integers automatically, so no special "BigInt" library is needed.

The final result will be a very large number, and we compute the sum of its decimal digits.