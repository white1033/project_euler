# Square Digit Chains

## Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,
$44 \to 32 \to 13 \to 10 \to 1 \to 1$
$85 \to 89 \to 145 \to 42 \to 20 \to 4 \to 16 \to 37 \to 58 \to 89$

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

## Analysis

The maximum sum of squared digits for a number below $10,000,000$ (i.e., up to $9,999,999$) occurs for $9,999,999$, which is $7 \times 9^2 = 7 \times 81 = 567$.

Therefore, any number below 10 million will immediately drop to a number $\le 567$ after the first step.
We can precompute the destination (1 or 89) for all numbers up to 567. Then for each number from 1 to 9,999,999, we compute the next term (which is $\le 567$) and look up its destination.

### Algorithm
1. Create an array `destinations` of size 568.
2. For $i$ from 1 to 567, simulate the chain until it hits 1 or 89. Store the result in `destinations[i]`.
3. Initialize `count = 0`.
4. Loop $n$ from 1 to 9,999,999:
   - Compute $s = \text{sum of squares of digits of } n$.
   - If `destinations[s] == 89`, increment `count`.
5. Return `count`.

### Further Optimization
We can observe that the order of digits doesn't matter for the sum of squares. For example, 12, 21, 102, 201 all map to $1^2+2^2+0^2 = 5$.
We could iterate combinations of digits instead of numbers, calculating the multinomial coefficient for how many numbers are formed by each combination.
However, since $N=10^7$ is relatively small, the direct iteration takes only a few seconds in Python and is simpler to implement.
