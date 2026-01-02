# Problem 36: Double-base Palindromes

## Problem Description

The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

## Analysis

A number is palindromic if it reads the same forwards and backwards. We need to check numbers $n < 1,000,000$.

### Key Observations

1.  **Binary Palindromes are Odd**:
    *   In binary, the most significant bit (MSB) is always 1 (no leading zeros).
    *   For a number to be a palindrome, the least significant bit (LSB) must match the MSB.
    *   Therefore, the LSB must be 1, which means the number must be **odd**.
    *   We can ignore all even numbers.

2.  **Search Space Density**:
    *   There are 500,000 odd numbers under 1,000,000.
    *   There are only roughly 2,000 decimal palindromes under 1,000,000.
    *   It is much faster to **generate** decimal palindromes and check if they are binary palindromes, rather than iterating all odd numbers and checking if they are decimal palindromes.

## Solution Approaches

### Approach 1: Brute Force (Filter)
Iterate through all odd numbers from 1 to 999,999.
1.  Check if $n$ is a palindrome in Base 10.
2.  If yes, convert to binary and check if it's a palindrome in Base 2.
3.  **Complexity**: $O(N)$ iterations.

### Approach 2: Generative (Constructive) - *Preferred*
Instead of checking every number, we construct decimal palindromes directly.
Since $N < 10^6$ (max 6 digits), we can create palindromes from a "root" number $k$ having up to 3 digits ($1 \le k < 1000$).

For each $k$:
1.  **Odd-length palindrome**: e.g., $k=12 \to 121$ (mirror all but last digit).
2.  **Even-length palindrome**: e.g., $k=12 \to 1221$ (mirror entire string).

**Algorithm**:
1.  Iterate $k$ from 1 to 999.
2.  Construct potential palindromes $P$.
3.  Filter: Keep $P$ only if $P < 1,000,000$.
4.  Filter: Keep $P$ only if $P$ is odd (Base 10 palindrome ending in even digit is an even number).
5.  Check: Is $P$ a palindrome in Base 2?
6.  Sum valid results.

**Complexity**: $O(\sqrt{N})$. We only generate and check $\approx 2000$ numbers.

## Performance Comparison

| Approach | Iterations | Time (approx) |
| :--- | :--- | :--- |
| Brute Force (Filter) | 500,000 | ~0.05s |
| **Generative** | **~2,000** | **~0.0005s** |

The generative approach is approximately **100x faster**.
