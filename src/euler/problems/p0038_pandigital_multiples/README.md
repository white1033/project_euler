# Problem 38: Pandigital Multiples

## Problem Description

Take the number $192$ and multiply it by each of $1, 2,$ and $3$:

$$
192 \times 1 = 192 \\
192 \times 2 = 384 \\
192 \times 3 = 576
$$

By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1, 2, 3)$.

The same can be achieved by starting with $9$ and multiplying by $1, 2, 3, 4,$ and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1, 2, 3, 4, 5)$.

What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1, 2, \dots, n)$ where $n > 1$?

## Analysis

We are looking for the largest 9-digit pandigital number formed by concatenating products.

### Constraints & Observations

1.  **Total Length**: The result must be exactly 9 digits.
2.  **Starting Digit**: Since we want the *largest* pandigital number, and we already know $918273645$ is a valid candidate (from the problem description), the answer must start with $9$.
    *   This implies our starting integer $X$ must also start with $9$.
3.  **Multiplier $n$**: We must multiply by at least $(1, 2)$, so $n \ge 2$.

### Narrowing the Search Space for $X$

Let's check possible lengths for the integer $X$ (which starts with 9):

*   **1-digit ($X=9$)**:
    *   Example given: $9 \times (1,2,3,4,5) \to 918273645$.
*   **2-digits ($90-99$)**:
    *   $n=3$: $X, 2X, 3X$. Since $X \ge 90$, products have lengths $2, 3, 3$. Total $2+3+3=8$. (Too short)
    *   $n=4$: Total $8+3=11$. (Too long)
*   **3-digits ($900-999$)**:
    *   $n=2$: $X, 2X$. Lengths $3, 4$ ($2 \times 900 = 1800$). Total $3+4=7$. (Too short)
    *   $n=3$: Total $7+4=11$. (Too long)
*   **4-digits ($9000-9999$)**:
    *   $n=2$: $X, 2X$. Lengths $4, 5$ ($2 \times 9000 = 18000$). Total $4+5=9$. **Possible!**
*   **5-digits ($10000+$)**:
    *   $n=2$: Lengths $5, 5$ (or more). Total $10+$. (Too long)

### Conclusion

The only search space capable of producing a **better** answer than the example ($918273645$) is **4-digit numbers starting with 9**.

We can iterate $X$ from $9876$ down to $9123$.
For each $X$, we calculate $S = \text{concat}(X, 2X)$.
If $S$ is pandigital, that is our answer (since we are searching from largest $X$, the resulting concatenated number starting with 9 will also be maximized).

## Solution

The algorithm iterates downwards through 4-digit numbers starting with 9, checks the concatenated product condition, and returns the first match.