# Problem 5: Smallest Multiple

## Description

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

[Link to Problem](https://projecteuler.net/problem=5)

## Analysis

We are looking for the Least Common Multiple (LCM) of the numbers $1, 2, \dots, 20$.

### Method 1: Iterative LCM
We can compute the LCM of a list of numbers sequentially using the property:
$$ \text{lcm}(a, b) = \frac{|a \cdot b|}{\text{gcd}(a, b)} $$
$$ \text{lcm}(1, \dots, n) = \text{lcm}(\text{lcm}(1, \dots, n-1), n) $$

### Method 2: Prime Factorization (Optimal)
The LCM of a set of numbers is the product of the highest powers of all prime factors involved.
For the range $1$ to $N$, for every prime $p \le N$, we find the largest exponent $k$ such that $p^k \le N$.

For $N=20$:
*   **Primes**: 2, 3, 5, 7, 11, 13, 17, 19
*   **Highest Powers**:
    *   $2^4 = 16$ (since $2^5 = 32 > 20$)
    *   $3^2 = 9$ (since $3^3 = 27 > 20$)
    *   $5^1 = 5$
    *   $7^1 = 7$
    *   $11^1 = 11$
    *   $13^1 = 13$
    *   $17^1 = 17$
    *   $19^1 = 19$

$$ \text{LCM} = 16 \times 9 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 $$

This method is extremely efficient as it involves no trial division or large number arithmetic until the final multiplication.