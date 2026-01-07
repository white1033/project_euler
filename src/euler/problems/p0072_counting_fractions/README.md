# Problem 72: Counting Fractions

Consider the fraction, $n/d$, where $n$ and $d$ are positive integers. If $n < d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:

$$1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8$$

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for $d \le 1,000,000$?

## Analysis

We want to find the number of reduced proper fractions $n/d$ with $d \le 1,000,000$.
A fraction $n/d$ is a reduced proper fraction if:
1.  $n < d$
2.  $\gcd(n, d) = 1$

For a fixed denominator $d$, the number of possible numerators $n$ is the count of positive integers less than $d$ that are coprime to $d$. This is exactly the definition of Euler's Totient Function, $\phi(d)$.

Since $n$ must be a positive integer, the smallest possible denominator is $d=2$ (since for $d=1$, $n < 1$ implies no positive integer solutions).

Therefore, the total number of reduced proper fractions for $d \le L$ is:
$$ \sum_{d=2}^{L} \phi(d) $$

We can compute $\phi(d)$ efficiently for all $d$ up to $1,000,000$ using a sieve method similar to the Sieve of Eratosthenes.

**Phi Sieve Algorithm:**
1.  Initialize $\phi[i] = i$ for all $i$.
2.  Iterate $i$ from 2 to $L$.
3.  If $\phi[i] == i$, then $i$ is prime.
    *   Update $\phi[i] = i - 1$.
    *   For all multiples $j = 2i, 3i, \dots$, update $\phi[j] = \phi[j] \times (1 - \frac{1}{i}) = \phi[j] - \frac{\phi[j]}{i}$.

Using this precomputed table, we simply sum the values from $\phi(2)$ to $\phi(1,000,000)$.

