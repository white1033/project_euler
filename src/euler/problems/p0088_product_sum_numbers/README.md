# Product-sum Numbers

## Problem 88

A natural number, $N$, that can be written as the sum and product of a given set of at least two natural numbers, $\{a_1, a_2, \dots, a_k\}$ is called a product-sum number: $N = a_1 + a_2 + \dots + a_k = a_1 \times a_2 \times \dots \times a_k$.

For example, $6 = 1 + 2 + 3 = 1 \times 2 \times 3$.

For a given set of size, $k$, we shall call the smallest $N$ with this property a minimal product-sum number. The minimal product-sum numbers for sets of size $k = 2, 3, 4, 5, 6$ are as follows:

- $k=2: 4 = 2 \times 2 = 2 + 2$
- $k=3: 6 = 1 \times 2 \times 3 = 1 + 2 + 3$
- $k=4: 8 = 1 \times 1 \times 2 \times 4 = 1 + 1 + 2 + 4$
- $k=5: 8 = 1 \times 1 \times 2 \times 2 \times 2 = 1 + 1 + 2 + 2 + 2$
- $k=6: 12 = 1 \times 1 \times 1 \times 1 \times 2 \times 6 = 1 + 1 + 1 + 1 + 2 + 6$

Hence for $2 \le k \le 6$, the sum of all the minimal product-sum numbers is $4+6+8+12 = 30$. Note that $8$ is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for $2 \le k \le 12$ is $\{4, 6, 8, 12, 15, 16\}$, the sum is $61$.

What is the sum of all the minimal product-sum numbers for $2 \le k \le 12000$?

## Analysis

For a set of numbers $\{a_1, \dots, a_m, 1, \dots, 1\}$ where there are $m$ numbers greater than 1 and $(k-m)$ ones, the condition is:
$$ P = \prod_{i=1}^m a_i = \sum_{i=1}^m a_i + (k-m) $$
Thus:
$$ k = P - \sum_{i=1}^m a_i + m $$

Since $a_i \ge 2$, the product $P$ grows much faster than the sum. The upper bound for a minimal product-sum number for a given $k$ is $2k$ (using the set $\{k, 2, 1, \dots, 1\}$). Since we need $k \le 12000$, the maximum minimal product-sum number is at most $24000$.

We can iterate through all combinations of factors $a_i$ such that their product $P \le 24000$. For each combination, we calculate the corresponding $k$. If $k \le 12000$, we update the minimal product-sum number for that $k$.

### Algorithm
1. Initialize an array `min_product_sum` of size 12001 with infinity.
2. Define a recursive function `find_factors(product, sum, depth, start)`:
   - Calculate $k = product - sum + depth$.
   - If $k \le 12000$:
     - `min_product_sum[k] = min(min_product_sum[k], product)`
   - Loop `i` from `start` such that `product * i <= 24000`:
     - Recurse: `find_factors(product * i, sum + i, depth + 1, i)`
3. Call `find_factors(1, 1, 1, 2)` (Wait, depth starts at 1 implies we have a dummy factor? Actually, simpler to handle the base case carefully. If we start with `product=1, sum=1, count=1` (representing a dummy starting state), then adding a factor `i` gives `product*i`, `sum+i`, `count+1`. The number of actual factors is `count-1` (excluding dummy). 
   - Let's adjust: Start with `product=1, sum=0, count=0`.
   - Adding `i`: `product=i`, `sum=i`, `count=1`.
   - $k = i - i + 1 = 1$. Not valid since $k \ge 2$.
   - We need at least 2 factors.
   - The code implementation handles this by checking $k$ only when we have enough factors or implicitly because small $k$ updates correctly. Actually, the formula $k = P - S + m$ assumes $m$ factors.
   - If we use the dummy start approach: `count` includes the dummy. So real factors $m = count - 1$.
   - Then $S_{real} = S_{curr} - 1$.
   - $k = P - (S - 1) + (count - 1) = P - S + count$.
   - Yes, the formula matches.
4. Collect all unique values from `min_product_sum[2:]`.
5. Return their sum.
