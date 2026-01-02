# Problem 49: Prime Permutations

## Problem Description

The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

## Analysis

We need to find a sequence of three numbers $(p_1, p_2, p_3)$ such that:
1.  All are 4-digit primes.
2.  All are permutations of each other (same digits).
3.  They form an arithmetic progression: $p_2 - p_1 = p_3 - p_2 = k$.

### Strategy: Grouping by Permutation (Fingerprinting)

Instead of checking permutations for every prime (which is slow), we group primes that are permutations of each other.

1.  **Generate Primes**: Find all primes between 1000 and 9999.
2.  **Fingerprint**: For each prime, sort its digits to form a key (e.g., $1487 \to "1478"$).
3.  **Group**: Store primes in a hash map (dictionary) where key is the fingerprint.
    *   `groups["1478"] = [1487, 4817, 8147, ...]`
4.  **Filter**: Keep only groups with at least 3 primes.
5.  **Find Progression**: For each valid group, check if any three numbers form an arithmetic progression.
    *   Iterate pairs $(a, b)$ from the sorted group.
    *   Calculate expected third term $c = b + (b - a)$.
    *   Check if $c$ exists in the group.
    *   If found, and it's not the example sequence $(1487, 4817, 8147)$, then it's our answer.

### Complexity
*   Number of 4-digit primes is small (1061).
*   Grouping is $O(N \cdot D \log D)$ where $N$ is number of primes, $D=4$ digits.
*   Checking progressions in small groups is very fast.

## Solution

The solution uses a dictionary to group primes by their digit composition and searches for arithmetic progressions within these groups.