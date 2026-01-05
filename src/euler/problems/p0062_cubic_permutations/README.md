# Problem 62: Cubic Permutations

## Description

The cube, $41063625$ ($345^3$), can be permuted to produce two other cubes: $56623104$ ($384^3$) and $66430125$ ($405^3$). In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

## Analysis

We are looking for a cube $C$ such that there are exactly 5 perfect cubes (including $C$ itself) that share the exact same digits (are permutations of each other).

### Approach

1.  **Signature**: We can define a "signature" for any number as its digits sorted in ascending order. For example, the signature of $41063625$ is `01234566`.
2.  **Grouping**: Any permutation of a number will have the same signature. Therefore, if two cubes are permutations of each other, they will map to the same signature.
3.  **Digit Length Constraint**: Since permutations must have the same number of digits (we don't count leading zeros for the original number, but the problem implies "permutations of its digits", and usually in Project Euler, the number of digits is preserved or we only care about the set of digits. However, a cube with $d$ digits cannot be a permutation of a cube with $d+1$ digits. So we can process cubes by their digit length (batch processing).
    *   Note: $0^3=0$, but we are looking for positive integers usually. $345^3$ is 8 digits.
    *   Usually "permutations" implies using all digits.
4.  **Algorithm**:
    *   Iterate through bases $n = 1, 2, 3, \dots$
    *   Calculate cube $c = n^3$.
    *   Determine the number of digits $L$.
    *   If $L$ is greater than the length of cubes we were currently collecting:
        *   Check the collected groups from the previous length.
        *   If any group has exactly 5 members, find the one with the smallest cube.
        *   If found, that is our answer (since we process lengths in increasing order, the first valid length we find will contain the smallest global answer).
        *   Clear the cache and start collecting for the new length $L$.
    *   Compute the signature of $c$ (e.g., sort digits).
    *   Add $c$ to the list of cubes for that signature.

### Example Walkthrough
For the problem example (target 3 permutations):
- We scan cubes.
- Eventually we reach 8-digit cubes.
- We find that $345^3, 384^3, 405^3$ all map to signature `01234566`.
- Once we finish 8-digit cubes, we see this group has size 3.
- If we were looking for size 3, we would return $345^3$ ($41063625$).

We simply extend this to look for size 5.