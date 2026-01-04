# Prime Pair Sets

## Problem Statement

[Problem 60](https://projecteuler.net/problem=60)

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

## Solution Analysis

### Graph Theory Approach (Clique Problem)
This problem can be modeled as finding a **clique of size 5** in a graph where:
*   **Vertices** are prime numbers.
*   **Edges** exist between two primes $p_i, p_j$ if both $concatenation(p_i, p_j)$ and $concatenation(p_j, p_i)$ are prime.

### Algorithm: Depth-First Search (Backtracking)
Since the clique size $K=5$ is small, we can use a recursive backtracking approach.

1.  **Candidate Generation**: Generate primes up to a certain limit (e.g., 10,000) using a sieve. Note that 2 and 5 can be excluded because concatenating them at the end of another number results in a composite number (divisible by 2 or 5).
2.  **Prime Pair Check**: A helper function `is_pair_prime(a, b)` checks if `int(str(a)+str(b))` and `int(str(b)+str(a))` are prime. We use the **Miller-Rabin** primality test for speed, as concatenated numbers can be large.
3.  **Recursive Search**:
    *   Iterate through the sorted list of primes.
    *   For each prime $p$, try to add it to the current set (clique).
    *   To add $p$, it must form a valid edge with **every** existing member of the set.
    *   If the set size reaches 5, we calculate the sum and return.

### Optimization
*   **Pruning**: We only search for candidates larger than the current largest element in the set to avoid duplicates and handle permutations.
*   **Memoization**: We cache the results of `is_pair_prime` to avoid re-checking the same pairs.
*   **Order**: Searching primes in ascending order helps find the "lowest sum" solution early.

### Complexity
Finding the Maximum Clique is generally NP-Hard. However, with the constraint of $N=5$ and the specific properties of primes, the search space is manageable. The graph is quite sparse (most pairs of primes do not concatenate to form primes).