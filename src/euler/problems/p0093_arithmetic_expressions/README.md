# Arithmetic Expressions

## Problem 93

By using each of the digits from the set, $\{1, 2, 3, 4\}$, exactly once, and making use of the four arithmetic operations ($+$, $-$, $*$, $/$), and parentheses/brackets, it is possible to form different positive integer targets.

For example,
$8 = \frac{4 \times (1 + 3)}{2}$
$14 = 4 \times (3 + 1 / 2)$
$19 = 4 \times (2 + 3) - 1$
$36 = 3 \times 4 \times (2 + 1)$

Note that concatenations of the digits, like $12 + 34$, are not allowed.

Using the set, $\{1, 2, 3, 4\}$, it is possible to obtain thirty-one different target numbers of which $36$ is the maximum, and each of the numbers $1$ to $28$ can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, $a < b < c < d$, for which the longest set of consecutive positive integers, $1$ to $n$, can be obtained, giving your answer as a string: $abcd$.

## Analysis

### Algorithm
1. Generate all combinations of 4 distinct digits from $\{0, 1, \dots, 9\}$. There are $\binom{10}{4} = 210$ sets.
2. For each set $\{a, b, c, d\}$:
   - Generate all permutations ($4! = 24$).
   - Generate all combinations of 3 operators from $\{+, -, *, /\}$ ($4^3 = 64$).
   - Apply all 5 possible groupings (bracket positions).
     - $((A \circ B) \circ C) \circ D$
     - $(A \circ (B \circ C)) \circ D$
     - $A \circ ((B \circ C) \circ D)$
     - $A \circ (B \circ (C \circ D))$
     - $(A \circ B) \circ (C \circ D)$
   - Compute the results using floating point arithmetic (checking for division by zero).
   - Filter for positive integers (using a small epsilon for float precision, e.g., `abs(x - round(x)) < 1e-9`).
3. Determine the length of the consecutive sequence $1, 2, \dots, n$ that can be formed.
4. Track the set that produces the maximum $n$.

### Complexity
- Sets: 210
- Permutations per set: 24
- Operator tuples: 64
- Groupings: 5
- Total operations: $210 \times 24 \times 64 \times 5 \approx 1.6 \times 10^6$.
- This is well within the capability of Python to solve in a few seconds.

### Implementation Details
- `itertools.combinations` for the sets.
- `itertools.permutations` for the digit orders.
- `itertools.product` for the operators.
- Nested try-except blocks for `ZeroDivisionError`.
