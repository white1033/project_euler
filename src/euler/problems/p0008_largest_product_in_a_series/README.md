# Largest Product in a Series

## Problem Statement

The four adjacent digits in the 1000-digit number that have the greatest product are $9 \times 9 \times 8 \times 9 = 5832$.

(The 1000-digit number is provided in the solution code)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

## Analysis

This is a classic sliding window problem.

We are given a large string of digits $S$ of length $N=1000$. We need to find the maximum product of a substring of length $K=13$.

### Algorithm
1.  Initialize `max_product` to 0.
2.  Iterate from index $i = 0$ to $N - K$.
3.  Extract the substring $S[i : i+K]$.
4.  If the substring contains '0', the product is 0. We can skip calculation (or even jump the index forward, but for $N=1000$ brute force is plenty fast).
5.  Otherwise, calculate the product of digits in the substring.
6.  Update `max_product` if the new product is greater.

### Optimization
Since we are looking for the *greatest* product, any sequence containing a zero will result in a product of 0. We can technically skip any window that contains a zero. A more advanced optimization would be to maintain a running product and divide by the leaving digit / multiply by the entering digit, handling zeros by resetting. However, given $K=13$ and $N=1000$, a simple $O(N \cdot K)$ approach is instant.

Complexity: $O(N \cdot K)$ where $N=1000, K=13$.
Operations $\approx 1000 \times 13 \approx 13,000$, which is negligible.