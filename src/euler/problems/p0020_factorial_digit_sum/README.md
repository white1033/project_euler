# Factorial Digit Sum

## Problem Statement

$n!$ means $n \times (n - 1) \times \dots \times 3 \times 2 \times 1$.

For example, $10! = 10 \times 9 \times \dots \times 3 \times 2 \times 1 = 3628800$,
and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.

Find the sum of the digits in the number $100!$.

## Analysis

This problem is very similar to Problem 16 (Power Digit Sum). We need to calculate a large number and sum its digits.

### Magnitude Estimation
$100!$ is a large number. We can estimate its magnitude using Stirling's formula or simply by summing logarithms:
$$ \log_{10}(100!) = \sum_{i=1}^{100} \log_{10}(i) \approx 157.97 $$
So $100!$ has approximately 158 digits.

### Algorithm
In Python, integers have arbitrary precision, limited only by available memory. 158 digits is trivial for Python to handle directly.

1.  Calculate $100!$ using `math.factorial` (or a simple loop).
2.  Convert the result to a string.
3.  Sum the digits.

### Complexity
*   **Time Complexity**: Calculating $N!$ takes roughly $O(N^2 \log N)$ or better depending on the multiplication algorithm. For $N=100$, it's negligible.
*   **Space Complexity**: $O(N \log N)$ bits to store the number.