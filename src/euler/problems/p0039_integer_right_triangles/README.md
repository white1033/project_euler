# Problem 39: Integer Right Triangles

## Problem Description

If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.
$\{20, 48, 52\}, \{24, 45, 51\}, \{30, 40, 50\}$

For which value of $p \le 1000$, is the number of solutions maximised?

## Analysis

We need to find the number of integer solutions for a given perimeter $p$.
Constraints:
1.  $a^2 + b^2 = c^2$ (Pythagorean theorem)
2.  $a + b + c = p$ (Perimeter)
3.  $a < b < c$ (Assume ordering to avoid duplicates)

### Algebraic Simplification

Instead of iterating $a, b, c$ ($O(p^2)$) or generating triples using Euclid's formula ($O(\sqrt{p})$ but complex), we can simplify the equations to check valid $b$ for a given $a$.

Substitute $c = p - a - b$ into $a^2 + b^2 = c^2$:
$$a^2 + b^2 = (p - a - b)^2$$
$$a^2 + b^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab$$
$$0 = p^2 - 2pa - 2pb + 2ab$$
$$2pb - 2ab = p^2 - 2pa$$
$$2b(p - a) = p(p - 2a)$$

$$b = \frac{p(p - 2a)}{2(p - a)}$$

### Search Strategy

1.  Iterate $p$ from 12 to 1000.
    *   **Optimization**: $p$ must be **even**. (Sum of 2 odds is even, sum of 2 evens is even; hypotenuse parity argument proves $p$ is always even).
2.  For each $p$, iterate $a$ from $1$ to $p/3$.
    *   Why $p/3$? Because $a$ is the smallest side. If $a > p/3$, then $b > a > p/3$ and $c > b > p/3$, so $a+b+c > p$.
3.  Calculate $b$ using the formula.
4.  If $b$ is an integer (numerator is divisible by denominator), we found a solution.

This reduces the complexity for each $p$ to $O(p)$, and total complexity to $O(p^2)$. With $p=1000$, this is trivial ($\approx 1.6 \times 10^5$ operations).

## Solution

The solution iterates through even perimeters, calculates potential side lengths using the derived formula, and tracks the maximum count.