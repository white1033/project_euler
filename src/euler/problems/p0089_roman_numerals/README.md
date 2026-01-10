# Roman Numerals

## Problem 89

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see [About... Roman Numerals](https://projecteuler.net/about=roman_numerals) for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

## Analysis

### Naive Approach (Parse and Reconstruct)

The most straightforward way to solve this is to:
1.  Parse each Roman numeral string into its integer value.
2.  Convert that integer back into a Roman numeral using the standard minimal rules (subtractive notation).
3.  Calculate the difference in length between the original string and the generated minimal string.

**Parsing Logic:**
Iterate through the string from right to left. Maintain the value of the previous character. If the current character's value is less than the previous one, subtract it; otherwise, add it.
Example: `IV`
- Right to left: `V` (5). Total = 5. Prev = 5.
- Next: `I` (1). 1 < 5, so Total = 5 - 1 = 4.

**Generation Logic:**
Greedily append the largest possible Roman numeral symbols (`M`, `CM`, `D`, `CD`, `C`, `XC`, `L`, `XL`, `X`, `IX`, `V`, `IV`, `I`) while subtracting their values from the target integer.

### String Replacement Approach (Optimization)

Alternatively, since the problem implies the input contains valid Roman numerals (just not minimal), we can look for patterns that can be shortened directly without converting to integers.

The non-minimal forms that can be shortened are sequences of additive characters that should be replaced by subtractive ones.
- `IIII` (4) $\to$ `IV` (Length 4 $\to$ 2, saved 2)
- `VIIII` (9) $\to$ `IX` (Length 5 $\to$ 2, saved 3)
- `XXXX` (40) $\to$ `XL` (Length 4 $\to$ 2, saved 2)
- `LXXXX` (90) $\to$ `XC` (Length 5 $\to$ 2, saved 3)
- `CCCC` (400) $\to$ `CD` (Length 4 $\to$ 2, saved 2)
- `DCCCC` (900) $\to$ `CM` (Length 5 $\to$ 2, saved 3)

By simply performing these string replacements in the correct order (handling the 9s before the 4s to avoid overlap issues like `VIIII` matching `IIII`), we can compute the saved characters directly.

However, the "Parse and Reconstruct" method is more general and verifies the correctness of the numeral values, so it is implemented here.

## Implementation

The solution reads `roman.txt`, computes the integer value for each line, generates the minimal string, and sums the difference in lengths.

```python
def roman_to_int(s):
    # Standard reverse iteration
    ...

def int_to_roman(n):
    # Greedy mapping
    ...
```
