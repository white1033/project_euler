# Powerful Digit Counts

## Problem Description

The 5-digit number, $16807 = 7^5$, is also a fifth power. Similarly, the 9-digit number, $134217728 = 8^9$, is a ninth power.

How many $n$-digit positive integers exist which are also an $n$-th power?

## Mathematical Analysis

We are looking for integers $x$ such that:
1. $x = a^n$ for some base $a$ and exponent $n$.
2. The number of digits in $x$ is exactly $n$.

The condition that $x$ has exactly $n$ digits can be expressed as:
$$ 10^{n-1} \le x < 10^n $$

Substituting $x = a^n$:
$$ 10^{n-1} \le a^n < 10^n $$

We can analyze this inequality by taking the base-10 logarithm ($\log_{10}$) of all parts:

### Upper Bound Analysis
$$ \log_{10}(a^n) < \log_{10}(10^n) $$
$$ n \cdot \log_{10}(a) < n $$

Assuming $n \ge 1$, we can divide by $n$:
$$ \log_{10}(a) < 1 $$
$$ a < 10^1 $$
$$ a < 10 $$

This tells us that the base $a$ must be a single-digit integer, i.e., $a \in \{1, 2, \dots, 9\}$.

### Lower Bound Analysis
$$ \log_{10}(10^{n-1}) \le \log_{10}(a^n) $$
$$ n - 1 \le n \cdot \log_{10}(a) $$

Rearranging to solve for $n$:
$$ n - n \cdot \log_{10}(a) \le 1 $$
$$ n(1 - \log_{10}(a)) \le 1 $$
$$ n \le \frac{1}{1 - \log_{10}(a)} $$

### Conclusion

For each valid base $a$ (from 1 to 9), the number of valid exponents $n$ is the largest integer satisfying the inequality derived above. Since $n$ represents a count starting from 1 (implied by the problem context, though technically $n=1$ works trivially for all $a$), the number of solutions for a given $a$ is:

$$ \text{Count}_a = \left\lfloor \frac{1}{1 - \log_{10}(a)} \right\rfloor $$

We simply sum these counts for $a = 1$ to $9$.

#### Example
For $a=9$:
$ n \le \frac{1}{1 - \log_{10}(9)} \approx \frac{1}{1 - 0.9542} \approx \frac{1}{0.0458} \approx 21.8 $
So for $a=9$, there are 21 values of $n$ (from 1 to 21) where $9^n$ has $n$ digits.

## Alternative Approaches

### Integer Iteration
While the logarithmic approach is efficient and mathematically elegant, we can also solve this using a direct simulation with Python's arbitrary-precision integers. This avoids any potential (though unlikely in this specific case) floating-point precision issues.

We iterate through each base $a \in [1, 9]$ and increment the power $n$ as long as the length condition holds.

```python
def solve_integer_only():
    count = 0
    for a in range(1, 10):
        n = 1
        while len(str(a**n)) == n:
            count += 1
            n += 1
    return count
```

### Comparison
*   **Logarithmic Method (Used)**: $O(1)$ complexity relative to the output magnitude. Extremely fast as it uses CPU floating-point instructions.
*   **Integer Iteration**: Robust and intuitive. It avoids floating-point arithmetic entirely but is slightly slower due to the cost of computing large powers and converting them to decimal strings (a relatively expensive operation).