# Problem 41: Pandigital Prime

## Problem Description

We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.

What is the largest $n$-digit pandigital prime that exists?

## Analysis

We want to find the largest pandigital prime. The maximum possible value for $n$ is 9.

### Divisibility Rule of 3
A number is divisible by 3 if the sum of its digits is divisible by 3.

Let's check the sum of digits for $n$-digit pandigital numbers:
*   **n=9**: Digits $1+2+3+4+5+6+7+8+9 = 45$. Since $45 \% 3 == 0$, all 9-digit pandigital numbers are divisible by 3. **Not prime.**
*   **n=8**: Digits $1+2+3+4+5+6+7+8 = 36$. Since $36 \% 3 == 0$, all 8-digit pandigital numbers are divisible by 3. **Not prime.**
*   **n=7**: Digits $1+2+3+4+5+6+7 = 28$. $28 \% 3 \ne 0$. **Possible primes.**
*   **n=6**: Sum = 21 (divisible by 3).
*   **n=5**: Sum = 15 (divisible by 3).
*   **n=4**: Sum = 10 (not divisible by 3).

### Search Strategy

Since we want the **largest**, we start searching with $n=7$.
We can generate all permutations of the digits $\{7, 6, 5, 4, 3, 2, 1\}$.
Since we want the largest, we generate them in **descending order** (starting with 7654321, then 7654312, etc.).
The first number we find that is prime will be our answer.

The number of permutations for $n=7$ is $7! = 5,040$. This is extremely small, allowing for instantaneous computation.

## Solution

The solution generates permutations of "7654321" in descending order and checks each for primality.