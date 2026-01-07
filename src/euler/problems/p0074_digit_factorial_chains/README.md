# Problem 74: Digit Factorial Chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
$$ 1! + 4! + 5! = 1 + 24 + 120 = 145 $$

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

$$ 169 \to 363601 \to 1454 \to 169 $$
$$ 871 \to 45361 \to 871 $$
$$ 872 \to 45362 \to 872 $$

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

$$ 69 \to 363600 \to 1454 \to 169 \to 363601 (\to 1454) $$
$$ 78 \to 45360 \to 871 \to 45361 (\to 871) $$
$$ 540 \to 145 (\to 145) $$

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

## Analysis

We need to calculate the chain length for each number from 1 to 999,999.
Since many chains merge (e.g., chains for 169, 363601, and 1454 involve the same loop), memoization is highly effective.

We define `next(n)` as the sum of factorials of digits of `n`.
For each `n`, we generate the sequence $n, next(n), next(next(n)), \dots$ until we encounter a number that has already been visited in the current chain (cycle detected) or a number whose chain length is already known (cache hit).

1.  **Cache Hit**: If we reach a number `x` already in `cache`, the length for the current number `n` is `(steps to x) + cache[x]`.
2.  **Cycle Detected**: If we reach a number `x` that is currently in our path (but not in cache), we have found a new cycle. 
    *   The numbers in the cycle have a chain length equal to the cycle length (number of unique terms).
    *   The numbers leading to the cycle have length equal to `(distance to cycle) + (cycle length)`.

We iterate through 1 to 1,000,000, populating the cache and counting how many have length 60.

Key optimization: Precompute factorials 0! to 9! to speed up `next(n)` calculation.
