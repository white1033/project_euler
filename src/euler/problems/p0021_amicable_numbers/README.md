# Amicable Numbers

## Problem Statement

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).
If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore $d(220) = 284$. The proper divisors of 284 are 1, 2, 4, 71 and 142; so $d(284) = 220$.

Evaluate the sum of all the amicable numbers under 10000.

## Analysis

We need to calculate the sum of proper divisors function, $\sigma_1(n) - n$, for all numbers up to 10,000.

### Divisor Sum Formula
If the prime factorization of $n$ is $p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, then the sum of all divisors $\sigma_1(n)$ is:
$$ \sigma_1(n) = \prod_{i=1}^k \frac{p_i^{e_i+1} - 1}{p_i - 1} $$
The sum of **proper** divisors is $d(n) = \sigma_1(n) - n$.

### Algorithm
1.  Iterate $a$ from 2 to 9999.
2.  Calculate $b = d(a)$.
3.  If $b > a$ (to avoid checking the same pair twice and to avoid perfect numbers where $a=b$):
    *   Calculate $d(b)$.
    *   If $d(b) == a$, then $(a, b)$ is an amicable pair.
    *   Add $a$ to the total sum.
    *   If $b < 10000$, add $b$ to the total sum as well.

### Complexity
*   **Time Complexity**: We perform factorization/divisor sum calculation for each number. With efficient factorization, this is fast. $O(N \sqrt{N})$ or better.
*   **Space Complexity**: $O(1)$ if calculated on the fly.