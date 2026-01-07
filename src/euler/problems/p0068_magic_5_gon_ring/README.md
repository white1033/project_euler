# Problem 68: Magic 5-gon ring

## Description
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to 9.

Working **clockwise**, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: `4,3,2; 6,2,1; 5,1,3`.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

| Total | Solution Set |
|:---:|:---|
| 9 | 4,2,3; 5,3,1; 6,1,2 |
| 9 | 4,3,2; 6,2,1; 5,1,3 |
| 10 | 2,3,5; 4,5,1; 6,1,3 |
| 10 | 2,5,3; 6,3,1; 4,1,5 |
| 11 | 1,4,6; 3,6,2; 5,2,4 |
| 11 | 1,6,4; 5,4,2; 3,2,6 |
| 12 | 1,5,6; 2,6,4; 3,4,5 |
| 12 | 1,6,5; 3,5,4; 2,4,6 |

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum **16-digit** string for a "magic" 5-gon ring?

## Analysis

### String Length Constraint
We have 10 numbers: 1 to 10.
- Digits 1-9 are 1 digit long.
- Digit 10 is 2 digits long.

The ring has 5 lines, each consisting of 3 numbers (1 Outer, 2 Inner).
Total numbers in the string = $5 \times 3 = 15$.
However, the 5 Inner numbers are repeated (each belongs to 2 lines), and the 5 Outer numbers appear once.
Wait, simpler view:
The string is the concatenation of 5 triplets.
Total length = (Digits in Outer nodes) + (Digits in Inner nodes * 2) - *Correction: The string is just formed by writing the numbers.*
Wait, the string is formed by writing the triplet $(O, I_a, I_b)$.
So length = $\sum \text{digits}(O_i) + \sum \text{digits}(I_{a,i}) + \sum \text{digits}(I_{b,i})$.
Actually, since each inner node is used exactly twice in the full set of lines, and each outer node exactly once:
Length = $\sum_{o \in Outer} \text{digits}(o) + 2 \times \sum_{i \in Inner} \text{digits}(i)$.

Total digits available in set $\{1..10\}$ is $9 \times 1 + 2 = 11$.
One number is 10 (2 digits), others are 1 digit.
Let $N_{10}$ be the position of the number 10.
- If 10 is **Outer**: It contributes 2 digits once.
  Length = $2 + 4 \times 1 + 2 \times (5 \times 1) = 6 + 10 = 16$.
- If 10 is **Inner**: It contributes 2 digits twice.
  Length = $5 \times 1 + 2 \times (2 + 4 \times 1) = 5 + 12 = 17$.

The problem asks for a **16-digit string**. Therefore, **10 must be in the Outer ring**.

### Search Space
We have 10 slots. The number of permutations is $10! = 3,628,800$.
This is small enough for a brute-force search.

**Optimization**:
1. **Constraint**: 10 must be in the Outer ring (to keep length 16).
2. **Symmetry**: The ring is rotationally symmetric. We can fix the position of 10 to be the first Outer node ($O_0$). This fixes one slot and leaves 9 slots to be permuted.
   Search space reduces to $9! = 362,880$.
   This provides a ~10x speedup.

## Implementation
1. Fix `p[0] = 10`.
2. Generate all permutations of numbers 1 to 9 for the remaining 9 positions.
3. For each permutation, check if it forms a magic ring (all line sums equal).
4. If magic, generate the string starting from the lowest outer node (clockwise).
5. Track the maximum string found.
