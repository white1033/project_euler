# Problem 3: Largest Prime Factor

## Description

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

[Link to Problem](https://projecteuler.net/problem=3)

## Analysis

We need to find the largest prime factor of $N = 600,851,475,143$.

### Trial Division Algorithm
The fundamental theorem of arithmetic states that every integer $n > 1$ can be uniquely represented as a product of prime numbers.

To find these factors, we can perform **Trial Division**:
1.  Initialize a divisor $d = 2$.
2.  While $d^2 \le N$:
    *   While $N \pmod d = 0$:
        *   $d$ is a prime factor.
        *   Divide $N$ by $d$: $N \leftarrow N / d$.
    *   Increment $d$. (Optimization: handle 2 separately, then skip even numbers).
3.  After the loop, if $N > 1$, the remaining $N$ is the largest prime factor.

### Complexity
The loop runs up to $\sqrt{N}$.
For $N \approx 6 \times 10^{11}$, $\sqrt{N} \approx 775,146$.
This is computationally trivial ($< 10^6$ operations).