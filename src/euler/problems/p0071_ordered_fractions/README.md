# Problem 71: Ordered Fractions

Consider fractions $n/d$, where $n$ and $d$ are positive integers. If $n < d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:

$$1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8$$

It can be seen that $2/5$ is the fraction immediately to the left of $3/7$.

By listing the set of reduced proper fractions for $d \le 1,000,000$ in ascending order of size, find the numerator of the fraction immediately to the left of $3/7$.

## Analysis

We are looking for the fraction $n/d$ such that $n/d < 3/7$ is maximized, with $d \le 1,000,000$.

The condition $n/d < 3/7$ is equivalent to:
$$ 7n < 3d $$
Since $n$ and $d$ are integers, $7n$ must be at most $3d - 1$:
$$ 7n \le 3d - 1 $$
$$ n \le \frac{3d - 1}{7} $$
$$ n = \left\lfloor \frac{3d - 1}{7} \right\rfloor $$

We want to find the fraction $n/d$ closest to $3/7$. The distance is:
$$ \frac{3}{7} - \frac{n}{d} = \frac{3d - 7n}{7d} $$

To minimize this distance, we need to minimize the numerator $3d - 7n$ and maximize the denominator $7d$. The smallest possible positive integer value for $3d - 7n$ is $1$.

If $3d - 7n = 1$, then $3d \equiv 1 \pmod 7$.
Multiplying by $5$ (the modular inverse of $3$ modulo $7$):
$$ 15d \equiv 5 \pmod 7 $$
$$ d \equiv 5 \pmod 7 $$

So, we are looking for the largest $d \le 1,000,000$ such that $d \equiv 5 \pmod 7$.

$$ 1,000,000 \div 7 = 142857 \text{ remainder } 1 $$
$$ 1,000,000 \equiv 1 \pmod 7 $$

Counting down:
*   $999,999 \equiv 0$
*   $999,998 \equiv 6$
*   $999,997 \equiv 5$

Thus, the optimal denominator is $d = 999,997$.
The corresponding numerator is:
$$ n = \frac{3(999,997) - 1}{7} = 428,570 $$
