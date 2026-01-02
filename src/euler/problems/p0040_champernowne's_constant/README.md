# Problem 40: Champernowne's Constant

## Problem Description

An irrational decimal fraction is created by concatenating the positive integers:

$$0.123456789101112131415161718192021...$$

It can be seen that the $12^{th}$ digit of the fractional part is $1$.

If $d_n$ represents the $n^{th}$ digit of the fractional part, find the value of the following expression.

$$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$

## Analysis

We need to find the digit at specific positions ($10^k$) in the sequence formed by concatenating positive integers.

### Approach: Range Estimation (Mathematical)

Instead of generating the string, we can calculate which number the $n$-th digit belongs to.

The sequence is built from:
*   1-digit numbers: $1 \dots 9$ (9 numbers, 9 digits total)
*   2-digit numbers: $10 \dots 99$ (90 numbers, 180 digits total)
*   3-digit numbers: $100 \dots 999$ (900 numbers, 2700 digits total)
*   ...
*   $k$-digit numbers: $9 \times 10^{k-1}$ numbers, $k \times 9 \times 10^{k-1}$ digits total.

### Algorithm to find $d_n$

1.  **Identify the Range**:
    Subtract the total digits of previous ranges from $n$ until $n$ is smaller than the size of the current range.
    *   Example for $n=12$:
        *   Range 1 (1-9): size 9. $12 > 9$, so $n \leftarrow 12 - 9 = 3$. We are in the 2-digit range.

2.  **Identify the Number**:
    In the $k$-digit range, the numbers start at $10^{k-1}$.
    The offset from the start is $\lfloor \frac{n-1}{k} \rfloor$.
    The target number is $\text{start} + \text{offset}$.
    *   Example ($n=3$, 2-digit range):
        *   Start = 10.
        *   Offset = $(3-1) // 2 = 1$.
        *   Target Number = $10 + 1 = 11$.

3.  **Identify the Digit**:
    The position within the number is $(n-1) \pmod k$.
    *   Example ($n=3$, 2-digit range):
        *   Index = $(3-1) \% 2 = 0$.
        *   Target Number is 11, index 0 is '1'.

### Complexity
*   **Time Complexity**: $O(\log n)$ (number of ranges is proportional to number of digits in $n$).
*   **Space Complexity**: $O(1)$.

This is far superior to the brute-force string generation method, which would require $O(n)$ memory and time. Although for $n=10^6$ brute force is feasible (~1MB), this mathematical approach works even for $n=10^{18}$.

## Solution

The solution implements the range estimation logic to directly compute the 7 required digits and multiply them.