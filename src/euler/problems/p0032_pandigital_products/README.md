# Pandigital Products

## Problem Statement

We shall say that an $n$-digit number is pandigital if it makes use of all the digits 1 to $n$ exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

## Analysis

Let the identity be $A \times B = P$.
We need to use digits $1-9$ exactly once. The total number of digits is 9.

### Digit Count Analysis
Let $D(n)$ be the number of digits of $n$.
$D(A) + D(B) + D(P) = 9$.
Also $D(P) = D(A) + D(B)$ or $D(A) + D(B) - 1$.

Let $X = D(A) + D(B)$. Then $D(P) = 9 - X$.
Substituting into product magnitude rules:
*   If $D(P) = X$, then $2X = 9 \implies X=4.5$ (impossible).
*   If $D(P) = X - 1$, then $2X - 1 = 9 \implies 2X = 10 \implies X=5$.
    Then $D(P) = 9 - 5 = 4$.

So the product **$P$ must have exactly 4 digits**.
This means $X = D(A) + D(B) = 5$.
The possible combinations for $(D(A), D(B))$ (assuming $A < B$) are:
1.  **1-digit $\times$ 4-digit**: ($1, 4$)
2.  **2-digit $\times$ 3-digit**: ($2, 3$)

### Algorithm
1.  Initialize a set `products` to store unique valid products.
2.  Iterate for Case 1 ($A \in [1, 9]$, $B \in [1000, 9999]$).
    *   Optimization: $P \le 9876$, so $B \le 9876/A$.
3.  Iterate for Case 2 ($A \in [10, 99]$, $B \in [100, 999]$).
    *   Optimization: $P \le 9876$, so $B \le 9876/A$.
4.  For each pair, calculate $P = A \times B$.
5.  Check if string "$A$ + $B$ + $P$" is a permutation of "123456789".
6.  If yes, add $P$ to `products`.
7.  Return sum of `products`.

### Complexity
The search space is very small due to the constraints.
*   Case 1: $9 \times \approx 2000$ checks.
*   Case 2: $90 \times \approx 100$ checks.
Total operations $< 20,000$. Very fast.