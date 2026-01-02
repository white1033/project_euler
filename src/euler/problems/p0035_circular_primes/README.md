# Circular Primes

## Problem Statement

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

## Analysis

We need to check primality for all rotations of primes below 1,000,000.

### Algorithm
1.  **Sieve**: Generate all primes up to 1,000,000 using Sieve of Eratosthenes. Store them in a `set` for $O(1)$ lookup.
2.  **Filter (Pruning)**:
    *   Any multi-digit circular prime cannot contain the digits `0, 2, 4, 6, 8` (because at some rotation, it would become an even number) or `5` (it would become divisible by 5).
    *   Therefore, we only need to check primes composed entirely of `1, 3, 7, 9` (plus the single-digit primes 2 and 5).
3.  **Check Rotations**:
    *   For each candidate prime, generate all its digit rotations.
    *   If all rotations exist in the prime set, count it.

### Complexity
*   **Time Complexity**: Sieve takes $O(N \log \log N)$. Checking each prime takes proportional to the number of digits $d$. Total complexity is dominated by the Sieve.
*   **Space Complexity**: $O(N)$ for the prime set.