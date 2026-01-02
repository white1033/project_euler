# Problem 50: Consecutive Prime Sum

## Problem Description

The prime $41$, can be written as the sum of six consecutive primes:
$$41 = 2 + 3 + 5 + 7 + 11 + 13$$

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains $21$ terms, and is equal to $953$.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

## Analysis

We need to find the longest sequence of consecutive primes whose sum is:
1.  Less than 1,000,000.
2.  A prime number itself.

### Search Strategy

1.  **Generate Primes**: Use a sieve to generate all primes up to 1,000,000. Store them in a list `primes` (for iteration) and a set `primes_set` (for $O(1)$ lookup).
2.  **Sliding Window / Accumulation**:
    *   We can iterate through all possible start positions $i$.
    *   From each start position, we accumulate the sum by adding subsequent primes.
    *   If the sum exceeds 1,000,000, we stop adding for this start position.
    *   If the sum is a prime (exists in `primes_set`) and the sequence length is greater than our current maximum found, we update the record.

### Optimization

*   **Sequence Length Limit**: The sum of the first 550 primes exceeds 1,000,000. This means the inner loop will only run at most $\approx 550$ times, not $N$ times.
*   **Total Complexity**: $O(N \cdot K)$, where $N$ is the number of primes ($\approx 78,000$) and $K$ is the max sequence length ($\approx 550$). This is roughly $4 \times 10^7$ operations, which is well within the time limit.

## Solution

The solution uses a sieve to generate primes and a nested loop to check sums of consecutive primes, tracking the maximum length found.