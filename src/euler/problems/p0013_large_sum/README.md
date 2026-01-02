# Large Sum

## Problem Statement

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(Numbers omitted for brevity, see solution source code)

## Analysis

This problem involves adding very large integers.
Most modern programming languages (like Python) handle arbitrary-precision integers automatically, so we can simply sum them up.

However, if we were working in a language with fixed-width integers (like C++ `long long`), we would only need to sum the **first 11-12 digits** of each number to get the first 10 digits of the result correctly, due to the carry-over from lower digits being relatively small.

### Estimation
We have 100 numbers, each roughly $10^{49}$.
The sum will be approximately $100 \times 10^{49} = 10^{51}$.
The maximum possible carry from the omitted 38+ digits would be negligible for the first 10 digits.

### Algorithm
1.  Parse the 100 numbers into a list.
2.  Calculate the sum.
3.  Convert the sum to a string and take the first 10 characters.
4.  Convert back to integer.