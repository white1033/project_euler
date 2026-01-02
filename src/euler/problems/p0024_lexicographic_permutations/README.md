# Lexicographic Permutations

## Problem Statement

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

$$012, 021, 102, 120, 201, 210$$

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

## Analysis

We need to find the $1,000,000$-th permutation of the digits $0-9$.
Total permutations = $10! = 3,628,800$.

### Method: Factorial Number System (Factoradic)
Instead of generating all permutations, we can directly construct the $N$-th permutation using the properties of factorials.

The first digit divides the total permutations into 10 blocks of size $9!$.
*   $0\dots$ covers indices $0$ to $9!-1$.
*   $1\dots$ covers indices $9!$ to $2 \times 9! - 1$.
*   ...

**Algorithm**:
1.  Target index $K = 1,000,000 - 1 = 999,999$ (0-based).
2.  Available digits $D = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]$.
3.  Iterate for each position (from left to right):
    *   Let $R$ be the number of remaining digits minus 1.
    *   Calculate block size $S = R!$.
    *   Find the index of the digit to pick: $idx = K // S$.
    *   Pick digit $D[idx]$ and append to result.
    *   Remove $D[idx]$ from $D$.
    *   Update $K = K \% S$.

### Example (0, 1, 2)
Find 4th permutation ($K=3$).
1.  $D=[0, 1, 2]$. $R=2$. $S=2!=2$.
    *   $idx = 3 // 2 = 1$.
    *   Pick $D[1] = \mathbf{1}$. $D=[0, 2]$.
    *   $K = 3 \% 2 = 1$.
2.  $D=[0, 2]$. $R=1$. $S=1!=1$.
    *   $idx = 1 // 1 = 1$.
    *   Pick $D[1] = \mathbf{2}$. $D=[0]$.
    *   $K = 1 \% 1 = 0$.
3.  $D=[0]$. $R=0$. $S=0!=1$.
    *   $idx = 0 // 1 = 0$.
    *   Pick $D[0] = \mathbf{0}$. $D=[]$.
    *   $K = 0 \% 1 = 0$.

Result: **120**. Checking the list: 012, 021, 102, **120**... Correct.

### Complexity
*   **Time Complexity**: $O(N^2)$ because deleting from a list is $O(N)$ and we do it $N$ times. With $N=10$, this is effectively $O(1)$.
*   **Space Complexity**: $O(N)$.