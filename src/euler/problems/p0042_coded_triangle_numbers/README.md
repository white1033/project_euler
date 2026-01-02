# Problem 42: Coded Triangle Numbers

## Problem Description

The $n^{th}$ term of the sequence of triangle numbers is given by, $t_n = \frac{1}{2}n(n+1)$; so the first ten triangle numbers are:

$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.

Using `words.txt`, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

## Analysis

We need to:
1.  Read a list of words from a file.
2.  Compute the value of each word ($A=1, \dots, Z=26$).
3.  Check if that value is a triangle number.

### Checking for Triangle Numbers

Given a number $x$, it is a triangle number if there exists an integer $n$ such that:
$$x = \frac{1}{2}n(n+1)$$
$$2x = n^2 + n$$
$$n^2 + n - 2x = 0$$

Using the quadratic formula to solve for $n$:
$$n = \frac{-1 \pm \sqrt{1^2 - 4(1)(-2x)}}{2}$$
$$n = \frac{-1 \pm \sqrt{1 + 8x}}{2}$$

Since $n$ must be positive, we take the positive root:
$$n = \frac{\sqrt{8x + 1} - 1}{2}$$

For $n$ to be an integer, two conditions must be met:
1.  $8x + 1$ must be a perfect square.
2.  The square root $\sqrt{8x + 1}$ must be odd (so that subtracting 1 yields an even number, divisible by 2).

This allows for an $O(1)$ check without pre-generating a list of triangle numbers.

## Solution

The solution parses the `words.txt` file, computes word values, and applies the inverse formula check to count triangle words.