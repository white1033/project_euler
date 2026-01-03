# Combinatoric Selections

## Problem Statement

There are exactly ten ways of selecting three from five, 12345:
$$ \binom{5}{3} = 10 $$

In general, $\binom{n}{r} = \frac{n!}{r!(n-r)!}$, where $r \le n$.

It is not until $n = 23$, that a value exceeds one-million: $\binom{23}{10} = 1144066$.

How many, not necessarily distinct, values of $\binom{n}{r}$ for $1 \le n \le 100$, are greater than one-million?

## Solution Analysis

### Mathematical Properties
The combination function $\binom{n}{r}$ (Pascal's Triangle) has two key properties that allow for significant optimization:

1.  **Symmetry**: $\binom{n}{r} = \binom{n}{n-r}$.
2.  **Unimodality**: For a fixed $n$, the sequence $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$ increases strictly until it reaches the middle, and then decreases strictly.

Visually, for a given $n$, the values look like a "mountain":
```text
      Peak
     /    \
   /        \
  /          \
 r_start    r_end
```

### Optimization Strategy
Instead of calculating all values, we only need to find the **"start of the peak"**.

1.  Iterate $n$ from 23 to 100.
2.  For each $n$, calculate $\binom{n}{r}$ starting from $r=1$ upwards.
3.  As soon as we find the first $r$ where $\binom{n}{r} > 1,000,000$, we stop. Let's call this $r_{start}$.
4.  Due to symmetry, the "end of the peak" is at $r_{end} = n - r_{start}$.
5.  All values between $r_{start}$ and $r_{end}$ (inclusive) are greater than 1,000,000.
6.  The count of such values for this row is:
    $$ \text{Count}_n = r_{end} - r_{start} + 1 = (n - r_{start}) - r_{start} + 1 = n + 1 - 2r_{start} $$

### Iterative Calculation
To avoid computing large factorials for every step, we use the multiplicative formula to update the value iteratively:
$$ \binom{n}{r} = \binom{n}{r-1} \times \frac{n - r + 1}{r} $$

This allows us to maintain a running value of the combination and detect the threshold immediately.

## Complexity
This approach is extremely efficient. For each $n$, we only iterate $r$ until we hit 1,000,000. Since combinations grow exponentially, we hit this limit very quickly (often $r \approx 4-10$), making the inner loop run in nearly constant time relative to $n$.