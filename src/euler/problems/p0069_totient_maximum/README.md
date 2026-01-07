# Problem 69: Totient Maximum

## Description
Euler's Totient function, $\phi(n)$ [sometimes called the phi function], is used to determine the number of numbers less than $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $\phi(9)=6$.

It can be seen that $n=6$ produces a maximum $n/\phi(n)$ for $n \le 10$.

| $n$ | Relative Primes | $\phi(n)$ | $n/\phi(n)$ |
|:---:|:---|:---:|:---|
| 2 | 1 | 1 | 2 |
| 3 | 1,2 | 2 | 1.5 |
| 4 | 1,3 | 2 | 2 |
| 5 | 1,2,3,4 | 4 | 1.25 |
| 6 | 1,5 | 2 | 3 |
| 7 | 1,2,3,4,5,6 | 6 | 1.1666... |
| 8 | 1,3,5,7 | 4 | 2 |
| 9 | 1,2,4,5,7,8 | 6 | 1.5 |
| 10 | 1,3,7,9 | 4 | 2.5 |

Find the value of $n \le 1,000,000$ for which $n/\phi(n)$ is a maximum.

## Analysis

The formula for Euler's Totient function is:
$$
\phi(n) = n \prod_{p|n} \left(1 - \frac{1}{p}\right)
$$
where the product is over distinct prime factors of $n$.

Substituting this into the ratio $n/\phi(n)$:
$$
\frac{n}{\phi(n)} = \frac{n}{n \prod_{p|n} (1 - 1/p)} = \frac{1}{\prod_{p|n} \frac{p-1}{p}} = \prod_{p|n} \frac{p}{p-1}
$$

To maximize this ratio, we need to maximize the product of $\frac{p}{p-1}$.
The term $\frac{p}{p-1}$ is always greater than 1, so multiplying by more prime factors always increases the ratio.
Furthermore, the function $f(p) = \frac{p}{p-1} = 1 + \frac{1}{p-1}$ is a decreasing function of $p$.
- For $p=2$, factor is 2.
- For $p=3$, factor is 1.5.
- For $p=5$, factor is 1.25.
- ...

Therefore, to maximize the ratio, we should select the **smallest consecutive primes** ($2, 3, 5, \dots$) until their product exceeds the limit $1,000,000$.

## Implementation
We simply multiply primes starting from 2 until the product exceeds $1,000,000$. The largest product under the limit is the answer.
