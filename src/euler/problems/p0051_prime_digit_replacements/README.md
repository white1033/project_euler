# Prime Digit Replacements

## Problem Statement

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

## Solution Analysis

To solve this efficiently, we can use a property of modular arithmetic concerning divisibility by 3.

### The "Modulo 3" Rule

A number is divisible by 3 if and only if the sum of its digits is divisible by 3.

Let $N$ be a number, and let $S$ be the sum of its digits.
If we replace $k$ identical digits $d$ with a new digit $d'$, the new sum of digits $S'$ becomes:
$$ S' = S - k \times d + k \times d' = S + k(d' - d) $$

The change in the sum is $k \times (d' - d)$.

Now consider the values modulo 3:
1.  **If $k$ is not divisible by 3**:
    *   As $d'$ increments by 1, the sum $S'$ changes by $k$.
    *   Since $k \not\equiv 0 \pmod 3$, the values of $S' \pmod 3$ will cycle through 0, 1, 2.
    *   This means that for every 3 consecutive digits substituted, at least one will result in a digit sum divisible by 3.
    *   If the digit sum is divisible by 3, the number is divisible by 3 (and thus composite, unless the number is 3 itself).
    *   In a set of 10 candidates (digits 0-9), we would inevitably have at least 3 composites (divisible by 3).
    *   Max primes possible = $10 - 3 = 7$.
    *   **Conclusion**: To get a family of 8 primes, **$k$ (the number of replaced digits) must be a multiple of 3**.

### Search Strategy

Since we are looking for the *smallest* prime, and the problem gives a 5-digit example with a 7-prime family, we can expect the answer to be a 5 or 6-digit number.

1.  **Iterate Primes**: Generate primes (e.g., using a Sieve) up to a reasonable limit (1,000,000).
2.  **Filter by Pattern**:
    *   We are looking for a pattern with $k=3$ replacements (smallest multiple of 3).
    *   We only need to check primes that have **three repeating digits** (e.g., three 0s, three 1s, etc.).
3.  **Optimization**:
    *   Since we need a family of 8 primes, we can afford at most $10 - 8 = 2$ non-primes.
    *   This implies that the smallest prime in the family *must* be formed by replacing the repeating digits with **0, 1, or 2**.
    *   Why? If the smallest prime was formed by replacing with '3', then '0', '1', and '2' must have been composite. That's 3 failures already, making it impossible to reach 8 primes.
    *   Therefore, we only check primes where the repeating digit is 0, 1, or 2.

### Algorithm

1.  Generate primes up to 1,000,000.
2.  For each prime `p`:
    *   Check digit counts.
    *   If `p` contains three `0`s, `1`s, or `2`s:
        *   Generate the 10 family members by replacing those digits.
        *   Count how many are prime.
        *   If count == 8, return the smallest prime in the family.