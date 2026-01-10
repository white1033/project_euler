# Large Non-Mersenne Prime

## Problem 97

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form $2^{6972593} - 1$; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form $2^p - 1$, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: $28433 \times 2^{7830457} + 1$.

Find the last ten digits of this prime number.

## Analysis

We need to calculate:
$$ (28433 \times 2^{7830457} + 1) \pmod{10^{10}} $$

### Algorithm
Using modular exponentiation, we can compute $2^{7830457} \pmod{10^{10}}$ efficiently.
Then we multiply by 28433 and add 1, taking modulo $10^{10}$ at each step to keep numbers small (though Python handles large integers automatically, the modulo keeps it efficient and focuses on the required digits).

Complexity: $O(\log E)$ where $E$ is the exponent.
