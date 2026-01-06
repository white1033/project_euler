# Odd Period Square Roots

## Problem Description

All square roots are periodic when written as continued fractions and can be written in the form:

$$ \sqrt{N} = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \dots}}} $$

For example, let us consider $\sqrt{23}$:
$$ \sqrt{23} = 4 + \sqrt{23} - 4 = 4 + \frac{1}{\frac{1}{\sqrt{23}-4}} = 4 + \frac{1}{1 + \frac{\sqrt{23}-3}{7}} $$

If we continue we would get the sequence:
$ \sqrt{23} = [4; (1, 3, 1, 8)] $, which has a period of length $4$.

Exactly how many continued fractions for $N \le 10000$ have an odd period?

## Mathematical Analysis

### Continued Fraction Algorithm for $\sqrt{N}$

For a non-square integer $N$, the continued fraction coefficients $a_0, a_1, a_2, \dots$ can be generated using the following iterative algorithm.

Let:
*   $m_0 = 0$
*   $d_0 = 1$
*   $a_0 = \lfloor \sqrt{N} \rfloor$

For $k \ge 0$:
1.  $m_{k+1} = d_k a_k - m_k$
2.  $d_{k+1} = \frac{N - m_{k+1}^2}{d_{k+1}}$ (Note: In implementation, we use $d_{k}$ from previous step for division, i.e., $d_{new} = (N - m_{new}^2) / d_{old}$)
3.  $a_{k+1} = \lfloor \frac{a_0 + m_{k+1}}{d_{k+1}} \rfloor$

### Period Detection
The sequence of coefficients $a_1, a_2, \dots$ is periodic. A specific property of the continued fraction of $\sqrt{N}$ is that the period ends immediately when we find a coefficient:
$$ a_k = 2a_0 $$

Using this property, we can simply iterate the algorithm until $a_k = 2a_0$ and count the number of steps $k$.

### Complexity
The length of the period is generally roughly $O(\sqrt{N} \log N)$. For $N=10000$, this computation is extremely fast using simple integer arithmetic.