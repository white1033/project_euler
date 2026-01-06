# Diophantine Equation

## Problem Description

Consider quadratic Diophantine equations of the form:
$$ x^2 - Dy^2 = 1 $$

For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13 \times 180^2 = 1$.

It can be assumed that there are no solutions in positive integers when $D$ is square.

By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain the following:
*   $3^2 - 2 \times 2^2 = 1$
*   $2^2 - 3 \times 1^2 = 1$
*   $9^2 - 5 \times 4^2 = 1$
*   $5^2 - 6 \times 2^2 = 1$
*   $8^2 - 7 \times 3^2 = 1$

Hence, by considering minimal solutions in $x$ for $D \le 7$, the largest $x$ is obtained when $D=5$.

Find the value of $D \le 1000$ in minimal solutions of $x$ for which the largest value of $x$ is obtained.

## Mathematical Analysis

This is the famous **Pell's Equation**.

### Theory
The fundamental solution $(x, y)$ to the equation $x^2 - Dy^2 = 1$ (where $D$ is not a perfect square) can be found using the **continued fraction expansion** of $\sqrt{D}$.

Let the convergents of the continued fraction of $\sqrt{D}$ be denoted by $h_k / k_k$.
The sequence of pairs $(h_k, k_k)$ provides the best rational approximations to $\sqrt{D}$.
Lagrange proved that the fundamental solution to Pell's equation is always one of these convergents.

Specifically:
1.  Generate the continued fraction coefficients $a_0, a_1, a_2, \dots$ for $\sqrt{D}$.
2.  Compute the sequence of convergents $h_k / k_k$ using the recurrence:
    *   $h_k = a_k h_{k-1} + h_{k-2}$
    *   $k_k = a_k k_{k-1} + k_{k-2}$
3.  The first pair $(h_k, k_k)$ that satisfies $h_k^2 - D k_k^2 = 1$ is the minimal solution.

### Algorithm
For each non-square $D \le 1000$:
1.  Initialize the continued fraction algorithm (as used in Problem 64).
2.  Initialize the convergent variables (as used in Problem 65).
3.  Iterate:
    *   Check if current convergent $(x, y)$ satisfies $x^2 - Dy^2 = 1$.
    *   If yes, record $x$, update global maximum if needed, and move to next $D$.
    *   If no, generate next coefficient $a$ and compute next convergent $(x, y)$.

### Why efficient?
While $x$ can grow very large (even exceeding 64-bit integers for $D < 1000$), Python handles arbitrary-precision integers automatically. The number of iterations corresponds to the length of the continued fraction period, which is relatively small ($O(\sqrt{D} \log D)$), so this approach is extremely fast.