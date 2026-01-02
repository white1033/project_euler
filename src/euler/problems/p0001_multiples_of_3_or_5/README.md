# Problem 1: Multiples of 3 or 5

## Description

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

[Link to Problem](https://projecteuler.net/problem=1)

## Analysis

We want to find the sum of all integers $x$ such that $1 \le x < 1000$ and ($x \pmod 3 = 0$ OR $x \pmod 5 = 0$).

### Method 1: Iteration
Loop through all numbers from 1 to 999 and check the divisibility condition. Complexity is $O(N)$.

### Method 2: Arithmetic Series (Inclusion-Exclusion)
We can calculate the sum of multiples of $k$ below $N$ using the arithmetic series formula.

Let $S_k$ be the sum of multiples of $k$ below $N$.
The terms are $k, 2k, 3k, \dots, m \cdot k$, where $m = \lfloor \frac{N-1}{k} \rfloor$.

Sum formula:
$$ S_k = k \times (1 + 2 + \dots + m) = k \times \frac{m(m+1)}{2} $$

By the Inclusion-Exclusion Principle:
$$ \text{Total Sum} = S_3 + S_5 - S_{15} $$

We subtract $S_{15}$ because multiples of 15 (LCM of 3 and 5) are counted in both $S_3$ and $S_5$.