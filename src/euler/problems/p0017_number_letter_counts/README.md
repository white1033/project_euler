# Number Letter Counts

## Problem Statement

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

**NOTE:** Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

## Analysis

We need to calculate the length of the English representation of numbers from 1 to 1000.

### Rules (British Usage)
1.  **1-9**: one, two, three, four, five, six, seven, eight, nine.
2.  **10-19**: ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen.
3.  **20-99**: twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety. (Combine with 1-9 for units).
4.  **100-999**: "X hundred".
    *   If not exact hundreds (e.g., 101, 150), add "and".
5.  **1000**: "one thousand".

### Word Lengths
*   **One**: 3, **Two**: 3, **Three**: 5, **Four**: 4, **Five**: 4, **Six**: 3, **Seven**: 5, **Eight**: 5, **Nine**: 4.
*   **Ten**: 3, **Eleven**: 6, **Twelve**: 6, **Thirteen**: 8, **Fourteen**: 8, **Fifteen**: 7, **Sixteen**: 7, **Seventeen**: 9, **Eighteen**: 8, **Nineteen**: 8.
*   **Twenty**: 6, **Thirty**: 6, **Forty**: 5, **Fifty**: 5, **Sixty**: 5, **Seventy**: 7, **Eighty**: 6, **Ninety**: 6.
*   **Hundred**: 7
*   **Thousand**: 8
*   **And**: 3

### Algorithm
We can simply iterate from 1 to 1000 and sum the lengths computed by a helper function `count_letters(n)`. This $O(N)$ approach is optimal given the small constraint ($N=1000$).