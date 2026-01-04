import pytest
from euler.problems.p0059_xor_decryption.solution import solve, decrypt, score_text

def test_decrypt_logic():
    """
    Test the XOR decryption logic with a known plaintext and key.
    """
    # Plaintext: "Hello"
    # Key: "abc" (cyclic)
    # 'H' ^ 'a' = 72 ^ 97 = 41
    # 'e' ^ 'b' = 101 ^ 98 = 7
    # 'l' ^ 'c' = 108 ^ 99 = 15
    # 'l' ^ 'a' = 108 ^ 97 = 13
    # 'o' ^ 'b' = 111 ^ 98 = 13
    
    plaintext = "Hello"
    key_chars = [ord('a'), ord('b'), ord('c')] # [97, 98, 99]
    cipher = [ord(c) ^ key_chars[i % 3] for i, c in enumerate(plaintext)]
    
    # Decrypting should return the ASCII of "Hello"
    decrypted_ascii = decrypt(cipher, key_chars)
    decrypted_text = "".join(chr(c) for c in decrypted_ascii)
    
    assert decrypted_text == plaintext

def test_score_text():
    """
    Test the scoring function.
    """
    text1 = "This is the best solution and it works."
    text2 = "Xjks lkjsdf lkjsdf lkj sfd"
    
    # Text1 should have a higher score because it contains " the ", " and "
    assert score_text(text1) > score_text(text2)

def test_solution():
    """Test the final solution for Problem 59."""
    # The answer is 129448
    assert solve() == 129448
