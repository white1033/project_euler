# Lychrel Numbers

## Problem Statement

If we take 47, reverse and add, $47 + 74 = 121$, which is palindromic.

Not all numbers produce palindromes so quickly. For example,
$349 + 943 = 1292$,
$1292 + 2921 = 4213$,
$4213 + 3124 = 7337$.

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.

How many Lychrel numbers are there below ten-thousand?

## Solution Analysis

This problem is a straightforward simulation.

### Algorithm
1.  Iterate through every number $n$ from 1 to 9,999.
2.  For each number, perform the "Reverse and Add" process.
    $$ n_{next} = n_{curr} + \text{reverse}(n_{curr}) $$
3.  Check if $n_{next}$ is a palindrome.
4.  If it is a palindrome within 50 iterations, it is **not** a Lychrel number.
5.  If we reach 50 iterations without finding a palindrome, we assume it **is** a Lychrel number.

### Note on "Less than 50 iterations"
The problem states "become a palindrome in less than fifty iterations".
This implies we perform the addition, check, and repeat. We do this loop 50 times. If the condition is met, we break.

### Efficiency
Since the limit is only 10,000 and max iterations is 50, the total operations are roughly $10,000 \times 50 = 500,000$ big integer additions. This is trivial for modern CPUs and Python's arbitrary-precision integers handle the growing numbers automatically.