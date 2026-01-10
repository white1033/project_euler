# Anagramic Squares

## Problem 98

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: $1296 = 36^2$. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: $9216 = 96^2$. We shall call CARE (and RACE) a square anagram word pair and specify that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using [words.txt](https://projecteuler.net/project/resources/p098_words.txt), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

## Analysis

### Algorithm
1.  **Parse Words**: Read `words.txt` and group words by their sorted character sets to find anagram pairs.
2.  **Generate Squares**: Generate all perfect squares up to the maximum number of digits found in the anagram pairs (which turns out to be 9 digits for words like `INTRODUCE`... actually typical max length is around 9-10).
3.  **Mapping**: For each anagram pair $(W_1, W_2)$ of length $L$:
    - Iterate through all squares $S_1$ of length $L$.
    - Create a mapping from letters of $W_1$ to digits of $S_1$.
    - Validate mapping:
        - Each letter maps to a unique digit.
        - No two letters map to the same digit.
    - Apply mapping to $W_2$ to get number $N_2$.
    - Check validity of $N_2$:
        - No leading zero ($W_2[0]$ mapping is not '0').
        - $N_2$ is a perfect square.
    - If valid, verify $N_2$ has same length (implicit if no leading zero) and update maximum square found.

### Optimization
- Group squares by length to reduce search space.
- Use sets for fast lookup of squares.
