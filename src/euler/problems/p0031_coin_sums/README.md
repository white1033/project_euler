# Coin Sums

## Problem Statement

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
$1 \times £1 + 1 \times 50p + 2 \times 20p + 1 \times 5p + 1 \times 2p + 3 \times 1p$

How many different ways can £2 be made using any number of coins?

## Analysis

This is a classic **Unbounded Knapsack Problem** (or Change Making Problem). We want to find the number of combinations of coins that sum up to a target value (200).

### Dynamic Programming Approach
Let `dp[i]` be the number of ways to make the amount `i`.
We initialize `dp[0] = 1` (one way to make 0: select nothing).

We iterate through each coin denomination $c$. For each coin, we update the `dp` table from $c$ to `target`:
`dp[i] = dp[i] + dp[i - c]`

This means the number of ways to make amount `i` using the current set of coins includes:
1.  Ways to make `i` without using the new coin (current value of `dp[i]`).
2.  Ways to make `i - c` using the new coin (value of `dp[i - c]`).

By iterating through coins one by one, we ensure that we don't count permutations (e.g., "1+2" and "2+1" are counted as the same combination).

### Complexity
*   **Time Complexity**: $O(N \times M)$, where $N$ is the target amount (200) and $M$ is the number of coin types (8). $200 \times 8 = 1600$ operations. Very fast.
*   **Space Complexity**: $O(N)$ for the DP array.