# Prime Power Triples

## Problem 87

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is $28$. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

$$28 = 2^2 + 2^3 + 2^4$$
$$33 = 3^2 + 2^3 + 2^4$$
$$49 = 5^2 + 2^3 + 2^4$$
$$47 = 2^2 + 3^3 + 2^4$$

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

## Analysis

We are looking for the number of distinct integers $n < 50,000,000$ such that $n = p_1^2 + p_2^3 + p_3^4$ where $p_1, p_2, p_3$ are primes.

The constraints on the primes are:
- $p_3^4 < 50,000,000 \implies p_3 < \sqrt[4]{50,000,000} \approx 84$
- $p_2^3 < 50,000,000 \implies p_2 < \sqrt[3]{50,000,000} \approx 368$
- $p_1^2 < 50,000,000 \implies p_1 < \sqrt{50,000,000} \approx 7071$

We can generate all primes up to $\approx 7100$ using a sieve. Then we can iterate through all valid combinations of $p_3, p_2, p_1$ and store the valid sums in a set to ensure uniqueness.

### Algorithm
1. Sieve primes up to 7100.
2. Precompute lists of squares, cubes, and fourth powers of primes that are below the limit.
3. Use nested loops to sum combinations.
4. Use a `set` to store unique sums found.
5. Return the size of the set.
