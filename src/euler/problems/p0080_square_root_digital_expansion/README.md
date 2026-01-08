# Problem 80: Square Root Digital Expansion

## Problem Description

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is $1.41421356237309504880\dots$, and the digital sum of the first one hundred decimal digits is $475$.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

[Link to Problem](https://projecteuler.net/problem=80)

## Analysis

We need to calculate the first 100 digits of $\sqrt{n}$ for non-perfect squares $n \le 100$.
Standard floating-point types (`float` or `double`) typically provide only 15-17 significant decimal digits, which is insufficient. We need **high-precision arithmetic**.

### Integer Arithmetic Approach
Since we want the first $P=100$ digits of $\sqrt{n}$, we can scale the number up to work with integers.
Recall that $\sqrt{n \times 10^{2k}} = \sqrt{n} \times 10^k$.
Calculating $\sqrt{n \times 10^{2k}}$ effectively shifts the decimal point of $\sqrt{n}$ by $k$ places to the right.

To get 100 digits, we can choose $k=100$ (or slightly more to avoid rounding errors at the last digit).
We compute the integer square root:
$$ X = \lfloor \sqrt{n \times 10^{200}} \rfloor $$
The integer $X$ will contain the first 100+ significant digits of $\sqrt{n}$.

### Filtering
We must skip perfect squares ($1, 4, 9, \dots, 100$) as their square roots are rational (integers) and have finite decimal expansions (or 0s after the decimal point), which the problem context implies we should ignore (or sum as is, but usually "irrational square roots" excludes integers).
Since there are 10 perfect squares up to 100, we perform the calculation for the remaining 90 numbers.

## Implementation

Python natively supports arbitrary-precision integers, making this straightforward.
We use `math.isqrt()` (available in Python 3.8+) for efficient integer square roots.

```python
import math

def calculate_digital_sum(n, precision=100):
    # Scale by 10^(2 * (precision + extra_buffer))
    # We use +10 buffer to be safe
    shift = 10 ** (2 * (precision + 10))
    root = math.isqrt(n * shift)
    
    # Convert to string and take first 100 digits
    digits = str(root)[:precision]
    return sum(int(d) for d in digits)
```
