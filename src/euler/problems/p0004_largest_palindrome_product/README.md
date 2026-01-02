# Problem 4: Largest Palindrome Product

## Description

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 \times 99$.

Find the largest palindrome made from the product of two 3-digit numbers.

[Link to Problem](https://projecteuler.net/problem=4)

## Analysis

We want to find $\max(a \times b)$ such that $100 \le a, b \le 999$ and $a \times b$ is a palindrome.

### Optimization 1: Search Order
Since we want the largest palindrome, we should iterate $a$ and $b$ from 999 downwards.
Also, we can assume $a \le b$ (or $b \le a$) to avoid duplicate checks.

### Optimization 2: Divisibility by 11
The product of two 3-digit numbers is at most $999 \times 999 = 998001$ (6 digits).
A 6-digit palindrome $P$ can be written as:
$$ P = 100000x + 10000y + 1000z + 100z + 10y + x $$
$$ P = 100001x + 10010y + 1100z $$
$$ P = 11(9091x + 910y + 100z) $$

This implies that any 6-digit palindrome is divisible by 11.
Since $P = a \times b$, at least one of $a$ or $b$ must be divisible by 11.

We can use this to optimize the inner loop. If $a$ is not divisible by 11, we only need to check $b$ where $b \equiv 0 \pmod{11}$.

### Algorithm
1.  Iterate $a$ from 999 down to 100.
2.  Iterate $b$ from $a$ down to 100.
    *   Optimization: If $a \times b \le \text{current\_max}$, break inner loop.
    *   Optimization: Apply the "mod 11" constraint to step size of $b$.
3.  Check if $a \times b$ is a palindrome.
4.  Update max.