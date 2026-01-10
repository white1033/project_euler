# Amicable Chains

## Problem 95

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
12496 $\to$ 14288 $\to$ 15472 $\to$ 14536 $\to$ 14264 ($\to$ 12496 $\to$ ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

## Analysis

### Algorithm
1.  **Divisor Sum Calculation**: We precompute the sum of proper divisors for all numbers up to 1,000,000. Using a sieve-like method is efficient:
    - Iterate $i$ from 1 to $N/2$.
    - Add $i$ to `sum_divs[j]` for all $j = 2i, 3i, \dots$.
    - Complexity is $O(N \log N)$.

2.  **Chain Traversal**: We iterate through each number $i$ from 2 to 1,000,000 to discover chains.
    - Follow the sequence $n_{k+1} = \text{sum\_divs}[n_k]$.
    - Stop if $n_{k+1} > 1,000,000$ or $n_{k+1}$ has been visited in the current path (cycle detected) or a previous path.
    - If a cycle is detected (i.e., we return to a number in the current path), extract the cycle portion.
    - Update the maximum length found so far and the smallest element of that cycle.

### Optimization
- Maintain a `visited` array. If we encounter a number that has been visited in a previous iteration, we can stop, because any cycle reachable from it would have already been found.
