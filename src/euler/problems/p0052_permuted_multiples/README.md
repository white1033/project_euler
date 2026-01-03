# Permuted Multiples

## Problem Statement

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, $x$, such that $2x, 3x, 4x, 5x$, and $6x$, contain the same digits.

## Solution Analysis

To find the smallest such integer efficiently, we can apply several mathematical constraints.

### 1. The Length Constraint
For $x$ and $6x$ to contain the exact same digits, they must have the **same number of digits**.

If $x$ has $d$ digits, then $10^{d-1} \le x < 10^d$.
For $6x$ to also have $d$ digits, it must be less than $10^d$.
$$ 6x < 10^d \implies x < \frac{10^d}{6} $$

This implies two things:
1.  The leading digit of $x$ must be **1**. (If it were $\ge 2$, then $2 \dots \times 6 = 12 \dots$, resulting in $d+1$ digits).
2.  We only need to search in the range $[10^{d-1}, \frac{10^d}{6}]$.

### 2. The Modulo 9 Constraint
A key property of permutations is that **the sum of their digits is invariant**.
If two numbers are permutations of each other, their digit sums are equal.
$$ S(x) = S(kx) $$

A number is congruent to the sum of its digits modulo 9.
$$ x \equiv S(x) \pmod 9 $$

Therefore:
$$ x \equiv S(x) = S(2x) \equiv 2x \pmod 9 $$
$$ x \equiv 2x \pmod 9 \implies x \equiv 0 \pmod 9 $$

This proves that **$x$ must be a multiple of 9**.
(This also holds for $3x, 4x, \dots$)

### Search Strategy
1.  Iterate through the number of digits $d$ starting from 1 (or 6, based on intuition/example, but starting from 1 is safer).
2.  For each $d$, search in the range $[10^{d-1}, \frac{10^d}{6}]$.
3.  Only check numbers divisible by 9 (step = 9).
4.  For each candidate $x$, verify if $2x, 3x, 4x, 5x, 6x$ are permutations of $x$. Checking $6x$ first is a good heuristic as it's most likely to violate the condition.

By combining these constraints, the search space is significantly reduced.