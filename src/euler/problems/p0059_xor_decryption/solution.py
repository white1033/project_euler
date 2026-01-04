import os
from collections import Counter
from euler.utils.common import timeit

def decrypt(cipher: list[int], key: list[int]) -> list[int]:
    """Decrypts the cipher using XOR with the given key (cyclic)."""
    decrypted = []
    key_len = len(key)
    for i, char in enumerate(cipher):
        decrypted.append(char ^ key[i % key_len])
    return decrypted

def score_text(text: str) -> int:
    """
    Scores the text based on the frequency of common English words.
    """
    score = 0
    common_words = [" the ", " and ", " of ", " to ", " a ", " in ", " is ", " that "]
    text_lower = text.lower()
    for word in common_words:
        score += text_lower.count(word)
    return score

def solve_brute_force(cipher: list[int]) -> int:
    """Original brute force solution."""
    best_score = -1
    best_decrypted_ascii = []
    
    for k1 in range(97, 123):
        for k2 in range(97, 123):
            for k3 in range(97, 123):
                key = [k1, k2, k3]
                decrypted_ascii = decrypt(cipher, key)
                try:
                    decrypted_text = "".join(chr(c) for c in decrypted_ascii)
                except ValueError:
                    continue
                
                current_score = score_text(decrypted_text)
                if current_score > best_score:
                    best_score = current_score
                    best_decrypted_ascii = decrypted_ascii

    return sum(best_decrypted_ascii)

def solve_frequency_analysis(cipher: list[int]) -> int:
    """
    Solves using frequency analysis.
    Assumption: The most frequent character in English text is space (ASCII 32).
    """
    key = [0, 0, 0]
    
    # Analyze each position in the key cycle (0, 1, 2)
    for i in range(3):
        # Extract characters encrypted by key[i]
        group = cipher[i::3]
        
        # Find the most frequent character in this group
        # In English, ' ' (space) is usually the most common character.
        # Encrypted_Char = Plain_Char ^ Key
        # => Key = Encrypted_Char ^ Plain_Char
        # => Key = Most_Freq_Encrypted ^ Space(32)
        
        counts = Counter(group)
        most_common_char, _ = counts.most_common(1)[0]
        
        derived_key_char = most_common_char ^ 32
        key[i] = derived_key_char
        
    # Decrypt with the derived key
    decrypted_ascii = decrypt(cipher, key)
    
    # Optional: Verify validity (check for "the")
    # decrypted_text = "".join(chr(c) for c in decrypted_ascii)
    # print(f"Derived Key: {[chr(k) for k in key]}")
    # print(f"Text Sample: {decrypted_text[:50]}...")
    
    return sum(decrypted_ascii)

@timeit
def solve() -> int:
    """
    Decrypts the XOR-encrypted message and returns the sum of ASCII values.
    Uses Frequency Analysis for O(N) performance.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cipher_path = os.path.join(current_dir, "0059_cipher.txt")
    
    with open(cipher_path, "r") as f:
        content = f.read().strip()
        cipher = [int(x) for x in content.split(",")]

    # We use the faster method by default
    return solve_frequency_analysis(cipher)

if __name__ == "__main__":
    print(solve())
