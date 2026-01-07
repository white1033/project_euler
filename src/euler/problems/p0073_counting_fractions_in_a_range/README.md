# Problem 73: Counting Fractions in a Range

Consider the fraction, $n/d$, where $n$ and $d$ are positive integers. If $n < d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:

$$1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, \mathbf{3/8, 2/5, 3/7}, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8$$

It can be seen that there are 3 fractions between $1/3$ and $1/2$.

How many fractions lie between $1/3$ and $1/2$ in the sorted set of reduced proper fractions for $d \le 12,000$?

## Analysis

We iterate through each denominator $d$ from 2 to 12,000.
For each $d$, we want to find the number of numerators $n$ such that:
$$ \frac{1}{3} < \frac{n}{d} < \frac{1}{2} $$
$$ \frac{d}{3} < n < \frac{d}{2} $$

This gives us the range for $n$:
$$ \lfloor \frac{d}{3} \rfloor + 1 \le n \le \lceil \frac{d}{2} \rceil - 1 $$
or more simply using integer division:
$$ n_{min} = (d // 3) + 1 $$
$$ n_{max} = (d - 1) // 2 $$

For each $n$ in this range, we check if $\gcd(n, d) == 1$. If so, it's a reduced proper fraction.

Since $d$ is only up to 12,000, a direct iteration is efficient enough.
The number of pairs to check is roughly:
$$ \sum_{d=1}^{12000} (\frac{d}{2} - \frac{d}{3}) = \sum \frac{d}{6} \approx \frac{1}{6} \frac{12000^2}{2} \approx 1.2 \times 10^7 $$
Checking 12 million GCDs is well within the 1-second timeframe for modern CPUs.

### Alternative Approaches (for larger limits)

1.  **Stern-Brocot Tree / Farey Sequence Recursion**
    We can generate fractions strictly between $1/3$ and $1/2$ using the mediant property.
    If $a/b$ and $c/d$ are adjacent terms in a Farey sequence, the next term between them is $(a+c)/(b+d)$.
    Starting with left=$1/3$ and right=$1/2$, we can recursively find the mediant $m = (1+1)/(3+2) = 2/5$.
    Then recurse on $(1/3, 2/5)$ and $(2/5, 1/2)$.
    The recursion stops when the denominator exceeds the limit.
    This effectively enumerates the Stern-Brocot tree in the relevant range.

2.  **Inclusion-Exclusion Principle (Mobius Inversion)**
    For a very large limit $L$ (e.g., $10^{10}$), we can calculate the total number of fractions (reduced or not) in the range:
    $$ T(L) = \sum_{d=2}^{L} (\lfloor \frac{d-1}{2} \rfloor - \lfloor \frac{d}{3} \rfloor) $$
    Let $R(L)$ be the count of reduced fractions.
    $$ R(L) = \sum_{k=1}^{L} \mu(k) \times (\text{Total fractions with denominator } \le \lfloor L/k \rfloor \text{ in range}) $$
    Actually, a simpler recursive formula is often used:
    $$ R(N) = T(N) - \sum_{k=2} R(\lfloor N/k \rfloor) $$
    This avoids explicit Mobius calculation but uses memoization.


