# Largest Exponential

## Problem 99

Comparing two numbers written in index form like $2^{11}$ and $3^7$ is not difficult, as any calculator would confirm that $2^{11} = 2048 < 3^7 = 2187$.

However, confirming that $632382^{518061} > 519432^{525806}$ would be much more difficult, as both numbers contain over three million digits.

Using [base_exp.txt](https://projecteuler.net/project/resources/p099_base_exp.txt), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

## Analysis

We want to find the pair $(b, e)$ that maximizes $b^e$.
Since the logarithm function is monotonically increasing for positive numbers, maximizing $b^e$ is equivalent to maximizing $\ln(b^e) = e \ln(b)$.

This avoids dealing with extremely large numbers directly and allows us to use standard floating-point arithmetic.

### Algorithm
1. Read `base_exp.txt` line by line.
2. For each line, parse base $b$ and exponent $e$.
3. Compute $v = e \ln(b)$.
4. Track the maximum $v$ and the corresponding line number.
