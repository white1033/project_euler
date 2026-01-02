# Non-Abundant Sums

## Problem Statement

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be $1 + 2 + 4 + 7 + 14 = 28$, which means that 28 is a perfect number.

A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.

As 12 is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

## Analysis

We are given an upper bound: 28123. All numbers greater than this can be written as the sum of two abundant numbers. We only need to check integers up to 28123.

### Algorithm

1.  **Find Abundant Numbers**:
    *   Iterate from 1 to 28123.
    *   Calculate `sum_proper_divisors(n)`.
    *   If sum > n, add to a list of `abundants`.

2.  **Mark Sums**:
    *   Create a boolean array (or set) `is_sum_of_two_abundants` of size 28124, initialized to False.
    *   Iterate through all pairs $(a_i, a_j)$ from the `abundants` list (where $j \ge i$).
    *   Calculate $S = a_i + a_j$.
    *   If $S \le 28123$, mark `is_sum_of_two_abundants[S] = True`.

3.  **Calculate Total Sum**:
    *   Iterate from 1 to 28123.
    *   If `is_sum_of_two_abundants[k]` is False, add $k$ to the total sum.

### Complexity
*   **Finding Abundants**: $O(N \sqrt{N})$ or slightly better with factorization. $N=28123$, so this is fast.
*   **Marking Sums**: Let $A$ be the count of abundant numbers. The complexity is $O(A^2)$. Since abundant numbers are somewhat dense (about 25%), $A \approx 7000$. $A^2 \approx 4.9 \times 10^7$, which is manageable (roughly 0.1 - 0.5 seconds in Python).