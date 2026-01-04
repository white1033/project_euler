# XOR Decryption

## Problem Statement

[Problem 59](https://projecteuler.net/problem=59)

The file `cipher.txt` contains the encrypted ASCII codes.
The encryption method is XOR with a 3-character lowercase key.
Find the sum of the ASCII values in the original text.

## Solution Analysis

### XOR Encryption
XOR (Exclusive OR) encryption works by applying the bitwise XOR operation between the message bytes and a key.
$$ C_i = M_i \oplus K_{i \pmod L} $$
where $C$ is the cipher text, $M$ is the message, $K$ is the key, and $L$ is the key length (3 in this case).

### Method 1: Brute Force (Naive)
The key consists of 3 lowercase English letters ($26^3 = 17,576$ combinations).
We can iterate through every possible key, decrypt the message, and check if the output contains common English words like " the " or " and ".

### Method 2: Frequency Analysis (Optimized)
Instead of guessing, we can derive the key.
1.  **Grouping**: Since the key length is 3, every 3rd character in the ciphertext is XORed with the same key character.
    *   Group 0: Characters at indices $0, 3, 6, \dots$ are encrypted with $K_0$.
    *   Group 1: Characters at indices $1, 4, 7, \dots$ are encrypted with $K_1$.
    *   Group 2: Characters at indices $2, 5, 8, \dots$ are encrypted with $K_2$.
2.  **Statistical Attack**: In normal English text, the most common character is usually the **Space** (` ` , ASCII 32), followed by 'e'.
3.  **Derivation**:
    Let $M_{freq}$ be the most frequent character in a plaintext group (likely space, 32).
    Let $C_{freq}$ be the most frequent character in the corresponding ciphertext group.
    $$ C_{freq} = M_{freq} \oplus K $$
    $$ K = C_{freq} \oplus 32 $$
4.  **Result**: This allows us to find the key in $O(N)$ time without trying 17,000 combinations.

### Complexity
*   **Brute Force**: $O(26^3 \cdot N) \approx 1.7 \times 10^4 \cdot N$ operations.
*   **Frequency Analysis**: $O(N)$ operations.

We implemented Method 2 for optimal performance.
