# Problem 46: Goldbach's Other Conjecture

## Problem Description

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

$$9 = 7 + 2 \times 1^2$$
$$15 = 7 + 2 \times 2^2$$
$$21 = 3 + 2 \times 3^2$$
$$25 = 7 + 2 \times 3^2$$
$$27 = 19 + 2 \times 2^2$$
$$33 = 31 + 2 \times 1^2$$

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

## Analysis

We are looking for the smallest odd composite $n$ such that there are no integer solutions for $p$ (prime) and $k$ (integer $>0$) in the equation:
$$n = p + 2k^2$$
$$p = n - 2k^2$$

### Search Strategy (Verification)

We iterate through odd numbers starting from 9 (first odd composite).
1.  Check if $n$ is prime. If so, skip (we only care about composites).
2.  If $n$ is composite, check if it fits the conjecture.
    *   Iterate $k$ from $1$ up to $\sqrt{n/2}$.
    *   Calculate $rem = n - 2k^2$.
    *   Check if $rem$ is prime.
    *   If we find any such $k$, the conjecture holds for $n$. Stop checking this $n$ and move to the next.
    *   If we try all possible $k$ and none result in a prime remainder, then $n$ is the counter-example.

### Complexity
For each $n$, we check $k \approx \sqrt{n}$ times.
Primality test is fast ($O(\sqrt{n})$ or better).
Overall complexity to find the answer $N$ is roughly $O(N \sqrt{N})$.
Since the answer is expected to be relatively small, this is highly efficient.

### Alternative Approach: Sieve
One could generate sums $p + 2k^2$ and mark them in a boolean array. The first "gap" in the array (at an odd composite index) would be the answer. However, this requires assuming an upper bound or dynamically resizing the array. The verification strategy is more robust for finding the *first* counter-example without bounds.

## Solution

The solution iterates through odd composites and verifies the conjecture for each by subtracting possible $2k^2$ terms and checking if the remainder is prime.