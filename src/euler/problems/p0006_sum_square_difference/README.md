# Problem 6: Sum Square Difference

## Description

The sum of the squares of the first ten natural numbers is,
$$ 1^2 + 2^2 + ... + 10^2 = 385 $$

The square of the sum of the first ten natural numbers is,
$$ (1 + 2 + ... + 10)^2 = 55^2 = 3025 $$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

[Link to Problem](https://projecteuler.net/problem=6)

## Analysis

We need to calculate two values for $n=100$:

1.  **Sum of the squares ($S_{sq}$)**:
    $$ S_{sq} = \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} $$

2.  **Square of the sum ($S_{sum}^2$)**:
    $$ S_{sum} = \sum_{i=1}^n i = \frac{n(n+1)}{2} $$
    $$ S_{sum}^2 = \left( \frac{n(n+1)}{2} \right)^2 $$

The result is $S_{sum}^2 - S_{sq}$.

### Complexity
Using the closed-form formulas, the calculation is $O(1)$.
Even with brute force iteration, it is $O(n)$, which is trivial for $n=100$.