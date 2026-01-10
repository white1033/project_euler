# Cube Digit Pairs

## Problem 90

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
[6][4]

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below 100: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.
{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} and {1, 2, 3, 4, 5, 9} is distinct from {1, 2, 3, 4, 5, 9} and {1, 2, 3, 4, 5, 6}.

But because we are placing the cubes side-by-side, the order of the cubes themselves does not matter?
Actually, the problem statement says:
"{1, 2, 3, 4, 5, 6} and {1, 2, 3, 4, 5, 9} is distinct from {1, 2, 3, 4, 5, 9} and {1, 2, 3, 4, 5, 6}." -> Wait.
Wait, let me re-read carefully.
"In determining a distinct arrangement we are interested in the digits on each cube, not the order."
This usually means the set on the cube.
Then it gives an example which is usually meant to clarify "set equality".
Wait, usually standard English "A and B is distinct from B and A" means order matters.
But if the cubes are identical objects in a set (pair of sets), then order doesn't matter.
Most interpretations of this problem (and the answer 1217) assume the pair of cubes is an unordered set of two sets.
If order mattered, the count would be roughly double (minus diagonal).
Given the phrasing "placing the two cubes side-by-side", usually implies we can swap them.
If I have Cube A and Cube B, and I want to display "01", I can put A=0, B=1 OR A=1, B=0.
The problem asks for "How many distinct arrangements of the two cubes allow for all square numbers...".
Usually this means unordered pairs of sets.
Let's assume unordered pairs.

## Analysis

### Naive Approach
1. Generate all combinations of 6 digits for a cube: $\binom{10}{6} = 210$.
2. Iterate through all pairs of combinations.
   - Total pairs (unordered, with replacement): $\frac{210 \times 211}{2} = 22,155$.
   - This is small enough to brute force.
3. For each pair of cubes $(C_1, C_2)$, check if all required squares can be formed.

### Rules
- Squares to form: 01, 04, 09, 16, 25, 36, 49, 64, 81.
- Extended digit matching:
  - If a cube contains 6, it counts as having 6 AND 9.
  - If a cube contains 9, it counts as having 9 AND 6.

### Implementation
We define a helper `has_digit(cube, d)` that implements the 6/9 rule.
Then we check each square $(d_1, d_2)$.
The condition is `(has(c1, d1) and has(c2, d2)) or (has(c2, d1) and has(c1, d2))`.

The loop structure:
```python
cubes = combinations(digits, 6)
n = len(cubes)
for i in range(n):
    for j in range(i, n):  # Start from i to handle unordered pairs + same cube case
        ...
```
