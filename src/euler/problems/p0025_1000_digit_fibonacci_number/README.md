# 1000-digit Fibonacci Number

## Problem Statement

The Fibonacci sequence is defined by the recurrence relation:
$$F_n = F_{n-1} + F_{n-2}, \text{ where } F_1 = 1 \text{ and } F_2 = 1.$$

The 12th term, $F_{12} = 144$, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Analysis

We need to find the smallest index $n$ such that $F_n \ge 10^{999}$.

### Method 1: Iteration (Brute Force)
Since Python handles large integers automatically, we can simply generate Fibonacci numbers until `len(str(F_n)) == 1000`. This is fast enough for 1000 digits.

### Method 2: Binet's Formula (Math)
$F_n$ can be approximated by:
$$ F_n \approx \frac{\phi^n}{\sqrt{5}} $$
where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.6180339887$.

We want to find $n$ such that:
$$ \frac{\phi^n}{\sqrt{5}} \ge 10^{999} $$

Taking $\log_{10}$ on both sides:
$$ \log_{10} \left( \frac{\phi^n}{\sqrt{5}} \right) \ge 999 $$
$$ n \log_{10} \phi - \log_{10} \sqrt{5} \ge 999 $$
$$ n \log_{10} \phi - 0.5 \log_{10} 5 \ge 999 $$
$$ n \ge \frac{999 + 0.5 \log_{10} 5}{\log_{10} \phi} $$

This allows us to calculate $n$ in $O(1)$ time.

### Calculation
*   $\log_{10} \phi \approx 0.20898764$
*   $0.5 \log_{10} 5 \approx 0.349485$
*   $n \ge \frac{999 + 0.349485}{0.20898764} \approx \frac{999.349485}{0.20898764} \approx 4781.859$

So $n = 4782$.