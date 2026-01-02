# Special Pythagorean Triplet

## Problem Statement

A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
$$a^2 + b^2 = c^2$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.
Find the product $abc$.

## Analysis

### Optimization with Euclid's Formula

We can generate Pythagorean triplets using Euclid's formula:
$$a = k(m^2 - n^2), \quad b = k(2mn), \quad c = k(m^2 + n^2)$$
where $m > n > 0$ and $k \ge 1$.

Given the sum constraint $a + b + c = S$:
$$S = k(m^2 - n^2) + k(2mn) + k(m^2 + n^2)$$
$$S = k(2m^2 + 2mn)$$
$$S = 2km(m+n)$$
$$\frac{S}{2} = km(m+n)$$

Let $S_{half} = S/2$. We need to find $m, n, k$ such that $km(m+n) = S_{half}$.

### Bounds and Complexity

Since $k \ge 1$ and $n > 0$:
$$m(m+n) \le S_{half}$$
$$m^2 < m(m+n) \le S_{half} \implies m < \sqrt{S_{half}}$$

For $S=1000$, $S_{half} = 500$, so $m < \sqrt{500} \approx 22.3$.
We only need to iterate $m$ from 2 to 22.

Inside the loop, we solve for $k$:
Let $R = S_{half} / m = k(m+n)$.
Since $0 < n < m$:
$$m < m+n < 2m$$
Substitute $m+n = R/k$:
$$m < R/k < 2m$$
$$\frac{R}{2m} < k < \frac{R}{m}$$

We iterate $k$ in this narrow range and check if it divides $R$. If it does, we find $n$ and calculate the triplet.

**Complexity**: $O(\sqrt{S})$. This is significantly faster than the $O(S)$ linear scan.
