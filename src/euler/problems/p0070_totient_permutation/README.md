# Problem 70: Totient Permutation

## Description
Euler's Totient function, $\phi(n)$, is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, $\phi(9)=6$.
The number 1 is considered to be relatively prime to every positive integer, so $\phi(1)=1$.

Interestingly, $\phi(87109)=79180$, and it can be seen that 87109 is a permutation of 79180.

Find the value of $n$, $1 < n < 10^7$, for which $\phi(n)$ is a permutation of $n$ and the ratio $n/\phi(n)$ produces a minimum.

## Analysis

We want to minimize the ratio $n/\phi(n)$.
Recall that:
$$
\frac{n}{\phi(n)} = \prod_{p|n} \frac{p}{p-1} = \prod_{p|n} \left(1 + \frac{1}{p-1}\right)
$$
To minimize this ratio, we should:
1.  Minimize the number of prime factors.
2.  Make the prime factors $p$ as large as possible (since $\frac{p}{p-1}$ decreases as $p$ increases).

The absolute minimum ratio occurs when $n$ is prime, in which case $\phi(n) = n-1$. However, $n$ and $n-1$ cannot be permutations of each other (their digit sums are not congruent modulo 9).

Therefore, the best candidates are numbers with **two large prime factors**: $n = p_1 \times p_2$.
For $n < 10^7$, we look for primes near $\sqrt{10^7} \approx 3162$.
If $p_1$ and $p_2$ are close to 3162, their product will be close to $10^7$ and their values will be as large as possible, minimizing the ratio.

## Implementation
1.  Generate primes in the range $[2000, 5000]$ (heuristically safe range around $\sqrt{10^7}$).
2.  Iterate through all pairs $(p_1, p_2)$ from this list.
3.  Calculate $n = p_1 \times p_2$. If $n > 10^7$, stop.
4.  Calculate $\phi(n) = (p_1-1)(p_2-1)$.
5.  Check if $\phi(n)$ is a permutation of $n$.
6.  Track the $n$ that produces the minimum ratio.
